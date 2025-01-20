import { applyFilters ,clear_all} from '/static/js/home_func.js';
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

  // Add event listeners to filters
  document.querySelectorAll('#job_type_filter input, #work_type_filter input, #salary_filter input, #posted_filter input').forEach((filter) => {
    filter.addEventListener('change', applyFilters);
  });

  document.getElementById('clear_all').addEventListener('click',clear_all)


  // console.log(id_for_current_exp)
  const experience_value = document.getElementById(id_for_current_exp)
  // Set the slider to the corresponding index if valid
  if (index !== -1) {
    slider.value = index;
    experience_value.classList.remove('visually-hidden')
  } 
  const spans = document.querySelectorAll(".exp_val");
    function updateExperienceLabel(value) {
        spans.forEach((span, index) => {
            if (index == value) {
                id_for_current_exp = "experience_value_"+index
                span.classList.remove("visually-hidden"); // Show the selected span
            } else {
                span.classList.add("visually-hidden"); // Hide other spans
            }
        });
    }

  slider.addEventListener("input", function () {
      updateExperienceLabel(this.value);
      applyFilters()
  });  
});

