function apply_job(jobId, button) {
    // Show loader and disable the button
    button.innerHTML = `
      <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    `;
    
    // Send an AJAX request to apply for the job
    fetch(`http://localhost:8000/dashboard/apply_job/${jobId}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(), // Add CSRF token for Django
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === "success") {
          // Change button text to "Applied" and keep it disabled
          button_disable();
        } else {
          // Handle error and re-enable the button
          button.innerHTML = "Apply now";
          button.disabled = false;
          alert("Failed to apply for the job. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        // Reset the button on error
        button.innerHTML = "Apply now";
        button.disabled = false;
        alert("An error occurred. Please try again.");
      });
  }

function button_disable(){
    console.log("Button disabled");
    const apply_button = document.querySelectorAll('.apply_button');
    apply_button.forEach(btn => {
        btn.disabled = true;
        btn.innerHTML = "Applied";
    });
}
  // Function to get CSRF token from cookies
function getCSRFToken() {
    const name = "csrftoken=";
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name)) {
            return cookie.substring(name.length);
        }
    }
    return "";
}

  const apply_div = document.querySelector('.apply_job_div');
  const stickyThreshold = 320; // The position where the sticky behavior starts
  
  window.addEventListener('scroll', () => {
      if (window.scrollY >= stickyThreshold) {
        apply_div.classList.remove('visually-hidden');
      } else {
        apply_div.classList.add('visually-hidden');
      }
  });
  