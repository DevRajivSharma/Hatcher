
$('#txtDate ').datepicker({
  format: "dd/mm/yyyy"
});
$('#exp_start_date  ').datepicker({
  format: "dd/mm/yyyy"
});
$('#exp_end_date ').datepicker({
  format: "dd/mm/yyyy"
});
$('#college_end_date ').datepicker({
  format: "dd/mm/yyyy"
});
$('#college_start_date ').datepicker({
  format: "dd/mm/yyyy"
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
const is_student_data = document.getElementById('is_student_data');
const school_medium = document.getElementById('school_medium');
function student() {
  schooling_detail.classList.remove(
    'visually-hidden',
  )
  school_medium.classList.add('visually-hidden');
  is_student.classList.remove('info-card');
  is_student.classList.add('active-info-card');
  no_student.classList.remove('active-info-card');
  no_student.classList.add('info-card');
  education_depend_label.innerHTML = 'What are you currently pursuing ?';
}
function non_student() {
  schooling_detail.classList.remove(
    'visually-hidden',
  )
  school_medium.classList.add('visually-hidden');
  no_student.classList.remove('info-card');
  no_student.classList.add('active-info-card');
  is_student.classList.remove('active-info-card');
  is_student.classList.add('info-card');
  education_depend_label.innerHTML = 'Select your highest education level';
}
function setEducationStatus(status) {
  const label = document.getElementById('is_student_data');
  label.setAttribute('data-educating', status);
}
is_student.addEventListener('click', () => {
  setEducationStatus('Yes');
  student();
})
no_student.addEventListener('click', () => {
  setEducationStatus('No');
  non_student();
})


const schoolingDetails = document.querySelectorAll('.schooling_details');
const degreeDivs = document.querySelectorAll('.degree_div'); // Select all degree divs
const college_detail_div = document.getElementById('college_detail_div');

schoolingDetails.forEach((span) => {
    span.addEventListener('click', function () {
        // Show the school medium div
        school_medium.classList.remove('visually-hidden');
        
        // Update the label with the selected education
        education_depend_label.setAttribute('data-higest-educaiton', span.innerHTML);
        console.log(span.innerHTML);

        // Remove 'active-info-card' class from all spans and add 'info-card' back
        schoolingDetails.forEach(s => {
            s.classList.remove('active-info-card');
            s.classList.add('info-card');
        });

        // Add 'active-info-card' class to the clicked span and remove 'info-card'
        this.classList.remove('info-card');
        this.classList.add('active-info-card');

        // Hide all degree divs initially
        degreeDivs.forEach(div => div.classList.add('visually-hidden'));

        // Show the corresponding degree div based on the selected info-card
        if (span.id === 'diploma') {
            document.getElementById('diploma_div').classList.remove('visually-hidden');
            college_detail_div.classList.remove('visually-hidden');
        } else if (span.id === 'iti') {
            document.getElementById('iti_div').classList.remove('visually-hidden');
            college_detail_div.classList.remove('visually-hidden');
        } else if (span.id === 'graduate') {
            document.getElementById('graudate_div').classList.remove('visually-hidden');
            college_detail_div.classList.remove('visually-hidden');
        } else if (span.id === 'p_graduate') {
            document.getElementById('post_graduate_div').classList.remove('visually-hidden');
            college_detail_div.classList.remove('visually-hidden');
        }
        else{
          college_detail_div.classList.add('visually-hidden');
        }
    });
});

function formatNumber(value) {
  // Remove non-numeric characters
  value = value.replace(/[^0-9]/g, '');
  
  // Add commas for thousands
  return value.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}


const have_experience = document.getElementById('have_experience')
const no_experience = document.getElementById('no_experience')
const experience_div =  document.getElementById('experience_div')
const is_experience = document.getElementById('is_experience')

have_experience.addEventListener('click',()=>{
  have_experience.classList.remove('info-card')
  have_experience.classList.add('active-info-card')
  no_experience.classList.remove('active-info-card')
  no_experience.classList.add('info-card')
  is_experience.setAttribute('data-experience','Yes')
  experience_div.classList.remove('visually-hidden')
})
no_experience.addEventListener('click',()=>{
  no_experience.classList.remove('info-card')
  no_experience.classList.add('active-info-card')
  have_experience.classList.remove('active-info-card')
  have_experience.classList.add('info-card')
  is_experience.setAttribute('data-experience','No')
  experience_div.classList.add('visually-hidden')
})

const working = document.getElementById('working')
const not_working = document.getElementById('not_working')
const notice_period = document.getElementById('notice_period')
const notice_period_is = document.getElementById('notice_period_is')
const is_working = document.getElementById('is_working')
const notice_periods = document.querySelectorAll('.notice_periods')

working.addEventListener('click',()=>{
  working.classList.remove('info-card')
  working.classList.add('active-info-card')
  not_working.classList.remove('active-info-card')
  not_working.classList.add('info-card')
  is_working.setAttribute('data-current_working','Yes')
  notice_period.classList.remove('visually-hidden')
})
not_working.addEventListener('click',()=>{
  not_working.classList.remove('info-card')
  not_working.classList.add('active-info-card')
  working.classList.remove('active-info-card')
  working.classList.add('info-card')
  is_working.setAttribute('data-current_working','No')
  notice_period.classList.add('visually-hidden')
})

notice_periods.forEach((span) => {
  span.addEventListener('click', function () {

      notice_period_is.setAttribute('data-notice-period',span.innerHTML)
      // Update the label with the selected education
      education_depend_label.setAttribute('data-higest-educaiton', span.innerHTML);
      console.log(span.innerHTML);

      // Remove 'active-info-card' class from all spans and add 'info-card' back
      notice_periods.forEach(s => {
          s.classList.remove('active-info-card');
          s.classList.add('info-card');
      });

      // Add 'active-info-card' class to the clicked span and remove 'info-card'
      this.classList.remove('info-card');
      this.classList.add('active-info-card');

})
})

const languages = [
  "Hindi", "Telugu", "Bengali", "Kannada", "Marathi", "Tamil",
  "Oriya", "Gujarati", "Malayalam", "Urdu", "Punjabi", "Assamese",
  "Nepali", "Kashmiri", "Maithili", "Rajasthani", "Haryanvi", "French",
  "German", "Spanish", "Japanese", "Mandarin"
];

const lang_collection = document.getElementById('lang_collection')

languages.forEach(lan =>{
  html = `<div class="lan-div lang-info">
                    <span style="margin-left: 3px;">${lan}</span>
                    <svg class="rotate_svg transition" xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="none" viewBox="0 0 16 16" class="add_cut_svg">
                      <path fill="black" d="M13.097 2.912a.806.806 0 00-1.141 0L8 6.86 4.044 2.904a.806.806 0 10-1.14 1.14L6.858 8l-3.956 3.956a.806.806 0 101.141 1.141L8 9.141l3.956 3.956a.806.806 0 101.14-1.14L9.142 8l3.956-3.956a.81.81 0 000-1.132z"></path>
                    </svg>
                </div>`
  lang_collection.insertAdjacentHTML('beforeend', html);
})

const lan_div = document.querySelectorAll('.lan-div')
const other_lan_div = document.getElementById('other_lan_div')
lan_div.forEach((lan,index)=>{
  lan.addEventListener('click',function(){
    current_lan = other_lan_div.getAttribute('data-other-lang')
    if (!current_lan == ''){
        current_lan = current_lan + ','
    }
    other_lan_div.setAttribute('data-other-lang',current_lan  + lan.querySelector('span').innerHTML)
    lan.classList.toggle('lang-info');
    lan.classList.toggle('active-lang-info');
    const svg = lan.querySelector('svg')
    svg.classList.toggle('rotate_svg')
    const path = lan.querySelector('svg path');
    const currentFill = path.getAttribute('fill');
    const newFill = currentFill === 'black' ? '#003C96' : 'black';
    path.setAttribute('fill', newFill);
  })
})

