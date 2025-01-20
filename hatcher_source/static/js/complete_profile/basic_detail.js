$(function () {
  $('#txtDate').datepicker({
      format: "dd/mm/yyyy"
  });
});
const button = document.querySelector("#get_loc");
button.addEventListener("click", (e) => {
    e.preventDefault()
    button.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
    navigator.geolocation.getCurrentPosition(position => {
        // Getting latitude & longitude from position obj
        const { latitude, longitude } = position.coords;

        // Getting location of passed coordinates using geocoding API
        const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`;

        fetch(url)
            .then(res => res.json())
            .then(data => {
                console.log(data.address.city)
                button.innerHTML = 'Pick Current Location';
                const location = document.getElementById('location');
                location.value = data.address.city 
            })
            .catch(() => {
                console.log("Error fetching data from API");
            });
    });
});

document.addEventListener('DOMContentLoaded', () => {
  const cityInput = document.getElementById('location');
  const suggestionsDiv = document.getElementById('city_suggestions');
  cityInput.addEventListener('input', () => {
      suggestionsDiv.classList.toggle = 'visually-hidden';
      const query = cityInput.value;
      // suggestionsDiv.classList.toggle('visually-hidden')
      if (query.length >= 1) {  // Start searching when 2+ characters are entered
        fetch(`/search_city/?term=${query}`)
        .then(response => response.json())
        .then(data => {
          console.log(data)
          suggestionsDiv.innerHTML = '';  // Clear previous suggestions
            if (data.length) {
              data.forEach(city => {
                const suggestion = document.createElement('div');
                suggestion.className = 'autocomplete-item';
                suggestion.textContent = city;

                // When a suggestion is clicked, fill the input and clear suggestions
                suggestion.addEventListener('click', () => {
                  cityInput.value = city;
                  suggestionsDiv.innerHTML = '';
                });

                suggestionsDiv.appendChild(suggestion);
              });
            } else {
              suggestionsDiv.innerHTML = '<div class="no-results">No cities found</div>';
            }
          });
      } else {
        suggestionsDiv.innerHTML = '';  // Clear suggestions if query is too short
      }
    });

    document.addEventListener('click', (e) => {
      if (!cityInput.contains(e.target) && !suggestionsDiv.contains(e.target)) {
        suggestionsDiv.innerHTML = '';
        suggestionsDiv.classList.add = 'visually-hidden'; // Hide suggestions
      }
    });

  });

const is_student = document.getElementById('student');
const no_student = document.getElementById('non_student');
const education_depend_label = document.getElementById('education_depend_label');
const schooling_detail = document.getElementById('schooling_detail');
function student(){
  schooling_detail.classList.remove(
    'visually-hidden',
  )
  is_student.classList.remove('info-card');
  is_student.classList.add('active-info-card');
  no_student.classList.remove('active-info-card');
  no_student.classList.add('info-card');
  education_depend_label.innerHTML = 'What are you currently pursuing ?';
}
function non_student(){
  schooling_detail.classList.remove(
    'visually-hidden',
  )
  no_student.classList.remove('info-card');
  no_student.classList.add('active-info-card');
  is_student.classList.remove('active-info-card');
  is_student.classList.add('info-card');
  education_depend_label.innerHTML = 'Select your highest education level';
}
is_student.addEventListener('click',()=>{
  student();
})
no_student.addEventListener('click',()=>{
  non_student();
  })


  const dropdown = document.querySelector('.custom-dropdown');
  const selected = dropdown.querySelector('.selected');
  const options = dropdown.querySelector('.options');
  
  selected.addEventListener('click', () => {
    dropdown.classList.toggle('active');
  });
  
  options.addEventListener('click', (event) => {
    if (event.target.tagName === 'LI') {
      selected.textContent = event.target.textContent;
      dropdown.classList.remove('active');
    }
  });
  