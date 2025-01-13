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
    const jobTypeElements = document.querySelectorAll('#job_type_filter input:checked');
    const jobType = Array.from(jobTypeElements).map(el => el.value).join(','); // Collect all selected job types
    console.log(jobType)
    const workType = document.querySelector('#work_type_filter input:checked')?.value || '';
    const salary = document.querySelector('#salary_filter input:checked')?.value || '';
    const postedIn = document.querySelector('#posted_filter input:checked')?.value || '';

    // Prepare the AJAX request
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/dashboard/job_search_ajax/?job_type=${jobType}&salary=${salary}&posted_in=${postedIn}&work_type=${workType}`, true);

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
        <div class="add_pad">
          <div class="card" id="card_id_contain" data-job-id="${job.id}" style="border-radius: 14px; cursor: pointer;" onclick="detail_job()">
            <div class="card-body">
              <div class="job_cards mb-2">
                <div class="job_cards">
                  <img src="/media/${job.company__image}" class="cmp_img" width="30px" height="30px" alt="image">
                  <div class="d-flex flex-column" style="margin-left: 10px;">
                    <span style="line-height: 14px; font-size: 20px;">${job.title}</span>
                    <span style="color: gray; font-size: 14px;">${job.company__name}</span>
                  </div>
                </div>
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#1F8268">
                  <path d="M8.355 6.316a.985.985 0 0 0 0 1.515l4.714 4.17-4.714 4.17a.985.985 0 0 0 0 1.515c.474.419 1.24.419 1.713 0l5.577-4.933a.985.985 0 0 0 0-1.515l-5.577-4.933c-.461-.408-1.239-.408-1.713.01Z"></path>
                </svg>
              </div>
              <div class="job_cards align-item-center" style="width: fit-content; align-items: center;">
                <img width="19px" height="auto" src="https://storage.googleapis.com/mumbai_apnatime_prod/jobs_page/Location_icon.webp" alt="">
                <span style="color: gray; font-size: 16px; margin-left: 5px;">${job.location}</span>
              </div>
              <div class="job_cards align-item-center" style="width: fit-content; align-items: center;">
                <img width="19px" height="auto" src="https://storage.googleapis.com/mumbai_apnatime_prod/jobs_page/Salary_icon.webp" alt="">
                <span style="color: gray; font-size: 16px; margin-left: 5px;">${job.salary}</span>
              </div>
              <div class="d-flex" style="margin-top: 10px;">
                ${job.req_skill_imp_skill ? `<div class="info-card rounded">${job.req_skill_imp_skill}</div>` : ''}
                ${job.work_type ? `<div class="info-card rounded">${job.work_type}</div>` : ''}
                ${job.job_type ? `<div class="info-card rounded">${job.job_type}</div>` : ''}
                ${job.experience ? `<div class="info-card rounded">${job.experience}</div>` : ''}
                ${job.perks ? `<div class="info-card rounded">${job.perks}</div>` : ''}
              </div>
              <p class="card-updated"><small class="text-body-secondary">${job.updated_at}</small></p>
            </div>
          </div>
        </div>
      `;
      jobListContainer.insertAdjacentHTML('beforeend', jobCard);
    });
  }

  // Add event listeners to filters
  document.querySelectorAll('#job_type_filter input, #work_type_filter input, #salary_filter input, #posted_filter input').forEach((filter) => {
    filter.addEventListener('change', applyFilters);
  });
});

