function apply_job(jobId, button) {
  button.innerHTML = `
    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
  `;

  const csrfToken = getCSRFToken();  // Fetch CSRF token

  fetch(`http://localhost:8000/dashboard/apply_job/${jobId}/`, {
      method: "POST",
      headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,  // Include CSRF token in request
      },
      credentials: "include",  // Ensures cookies are sent with the request
  })
  .then((response) => response.json())
  .then((data) => {
      if (data.status === "success") {
          button_disable();
      } else {
          button.innerHTML = "Apply now";
          button.disabled = false;
          alert("Failed to apply for the job. Please try again.");
      }
  })
  .catch((error) => {
      console.error("Error:", error);
      button.innerHTML = "Apply now";
      button.disabled = false;
      alert("An error occurred. Please try again.");
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
function button_disable(){
    console.log("Button disabled");
    const apply_button = document.querySelectorAll('.apply_button');
    apply_button.forEach(btn => {
        btn.disabled = true;
        btn.innerHTML = "Applied";
    });
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
  