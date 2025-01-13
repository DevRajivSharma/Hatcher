document.querySelectorAll('.toggle_arrow').forEach(arrow => {
    arrow.addEventListener('click', () => {
      arrow.classList.toggle('rotate');
      const targetId = arrow.getAttribute('data-toggle-div');
      const targetDiv = document.getElementById(targetId);
      if (targetDiv) {
        targetDiv.classList.toggle('visually-hidden');
      }
    });
  });

document.addEventListener('DOMContentLoaded', () => {
  // Function to handle filter application
  function applyFilters() {
    // Collect filter values
    const jobType = document.querySelector('#work_type_filter input:checked')?.id || '';
    const salary = document.querySelector('#salary_filter input:checked')?.value || '';
    const postedIn = document.querySelector('#posted_filter input:checked')?.value || '';

    // Prepare the AJAX request
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/dashboard/job_search_ajax/?job_type=${jobType}&salary=${salary}&posted_in=${postedIn}`, true);

    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

    // Handle the response
    xhr.onload = function () {
      if (xhr.status === 200) {
        const data = JSON.parse(xhr.responseText);
        updateJobListings(data.jobs);
      } else {
        console.error('Failed to fetch filtered jobs');
      }
    };

    // Send the request
    xhr.send();
  }

  // Function to update job listings dynamically
  function updateJobListings(jobs) {
    const jobListContainer = document.getElementById('job-list-container');
    jobListContainer.innerHTML = ''; // Clear existing job listings

    jobs.forEach((job) => {
      const jobCard = `
        <div class="job-card">
          <img src="${job.company__image}" alt="${job.company__name}" class="company-logo">
          <h3>${job.title}</h3>
          <p><strong>Company:</strong> ${job.company__name}</p>
          <p><strong>Location:</strong> ${job.location}</p>
          <p><strong>Salary:</strong> ${job.salary}</p>
          <p><strong>Job Type:</strong> ${job.job_type}</p>
        </div>
      `;
      jobListContainer.insertAdjacentHTML('beforeend', jobCard);
    });
  }

  // Add event listeners to filters
  document.querySelectorAll('#work_type_filter input, #salary_filter input, #posted_filter input').forEach((filter) => {
    filter.addEventListener('change', applyFilters);
  });
});

