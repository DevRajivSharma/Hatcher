
$('#birth_date').datepicker({
  format: "yyyy-mm-dd",
  endDate: new Date(new Date().setFullYear(new Date().getFullYear() - 18)), // Set max date to 18 years ago
  autoclose: true,
  todayHighlight: true
});

$('#exp_start_date  ').datepicker({
  format: "yyyy-mm-dd"
});
$('#exp_end_date ').datepicker({
  format: "yyyy-mm-dd"
});
$('#college_end_date ').datepicker({
  format: "yyyy-mm-dd"
});
$('#college_start_date ').datepicker({
  format: "yyyy-mm-dd"
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
    else {
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
const experience_div = document.getElementById('experience_div')
const is_experience = document.getElementById('is_experience')

have_experience.addEventListener('click', () => {
  have_experience.classList.remove('info-card')
  have_experience.classList.add('active-info-card')
  no_experience.classList.remove('active-info-card')
  no_experience.classList.add('info-card')
  is_experience.setAttribute('data-experience', 'Yes')
  experience_div.classList.remove('visually-hidden')
})
no_experience.addEventListener('click', () => {
  no_experience.classList.remove('info-card')
  no_experience.classList.add('active-info-card')
  have_experience.classList.remove('active-info-card')
  have_experience.classList.add('info-card')
  is_experience.setAttribute('data-experience', 'No')
  experience_div.classList.add('visually-hidden')
})

const working = document.getElementById('working')
const not_working = document.getElementById('not_working')
const notice_period = document.getElementById('notice_period')
const notice_period_is = document.getElementById('notice_period_is')
const is_working = document.getElementById('is_working')
const notice_periods = document.querySelectorAll('.notice_periods')

working.addEventListener('click', () => {
  working.classList.remove('info-card')
  working.classList.add('active-info-card')
  not_working.classList.remove('active-info-card')
  not_working.classList.add('info-card')
  is_working.setAttribute('data-current_working', 'Yes')
  notice_period.classList.remove('visually-hidden')
})
not_working.addEventListener('click', () => {
  not_working.classList.remove('info-card')
  not_working.classList.add('active-info-card')
  working.classList.remove('active-info-card')
  working.classList.add('info-card')
  is_working.setAttribute('data-current_working', 'No')
  notice_period.classList.add('visually-hidden')
})

notice_periods.forEach((span) => {
  span.addEventListener('click', function () {

    notice_period_is.setAttribute('data-notice-period', span.innerHTML)
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

languages.forEach(lan => {
  html = `
  <div class="lan-div lang-info">
                    <span style="margin-left: 3px;">${lan}</span>
                    <svg class="rotate_svg transition" xmlns="http://www.w3.org/2000/svg" width="13" height="13" fill="none" viewBox="0 0 16 16" class="add_cut_svg">
                      <path fill="black" d="M13.097 2.912a.806.806 0 00-1.141 0L8 6.86 4.044 2.904a.806.806 0 10-1.14 1.14L6.858 8l-3.956 3.956a.806.806 0 101.141 1.141L8 9.141l3.956 3.956a.806.806 0 101.14-1.14L9.142 8l3.956-3.956a.81.81 0 000-1.132z"></path>
                    </svg>
          </div>`
  lang_collection.insertAdjacentHTML('beforeend', html);
})

const lan_div = document.querySelectorAll('.lan-div')
const other_lan_div = document.getElementById('other_lan_div')
const other_lang_inp = document.getElementById('other_lang_inp')
lan_div.forEach((lan, index) => {
  lan.addEventListener('click', function () {

    current_lan = other_lan_div.getAttribute('data-other-lang')
    if (!current_lan == '') {
      current_lan = current_lan + ','
    }
    other_lan_div.setAttribute('data-other-lang', current_lan + lan.querySelector('span').innerHTML)
    curren_val = other_lang_inp.value
    if (!curren_val == '') {
      curren_val = curren_val + ','
    }
    other_lang_inp.value = curren_val + lan.querySelector('span').innerHTML
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



const progressSteps = document.querySelectorAll(".progress-step");
const progressBarFill = document.querySelector(".progress-bar-fill");
const prevButton = document.getElementById("prev");
const nextButton = document.getElementById("next");
const complete_profile_form = document.getElementById('complete_profile_form');
const sections = document.querySelectorAll(".detail_container");
const submit = document.getElementById('submit');
submit.addEventListener('click',()=>{
  complete_profile_form.submit()
})
let currentIndex = 0; // Tracks the currently visible section
let currentStep = 1;

function next_page() {
  if (currentIndex == 0) {
    // if (validate_basic_detail()){
    if (true) {
      if (currentIndex < sections.length - 1) {
        currentIndex++;
        complete_profile_form.style.marginLeft = `-${currentIndex * 100}%`;
        return true;
      }
    }
    else {
      return false;
    }
  }
  else if (currentIndex == 1) {
    // if (validateEducationForm()) {
      if (true){
      if (currentIndex < sections.length - 1) {
        currentIndex++;
        complete_profile_form.style.marginLeft = `-${currentIndex * 100}%`;
        return true;
      }
    }
    else {
      return false;
    }
  }
  else if (currentIndex == 2) {
    // if (validateExperienc()) {
      if (true){
      if (currentIndex < sections.length - 1) {
        currentIndex++;
        complete_profile_form.style.marginLeft = `-${currentIndex * 100}%`;
        return true;
      }
    }
    else {
      return false;
    }
  }
  else if (currentIndex == 3) {
    // if (validateLanguage()) {
      if (true){
      if (currentIndex < sections.length - 1) {
        currentIndex++;
        complete_profile_form.style.marginLeft = `-${currentIndex * 100}%`;
        return true;
      }
    }
    else {
      return false;
    }
  }
  else if (currentIndex == 4) {
    if (validateJobPrefference()) {
      // if (true){
      if (currentIndex < sections.length - 1) {
        currentIndex++;
        complete_profile_form.style.marginLeft = `-${currentIndex * 100}%`;
        return true;
      }
    }
    else {
      return false;
    }
  }
}

function previous_page() {
  if (currentIndex > 0) {
    currentIndex--;
    complete_profile_form.style.marginLeft = `-${currentIndex * 100}%`; // Slide to the previous section
  }
}

function updateProgress() {
  // Update active steps
  progressSteps.forEach((step, index) => {
    if (index < currentStep) {
      step.classList.add("active");
    } else {
      step.classList.remove("active");
    }
  });

  // Update progress bar fill
  const progressPercentage = ((currentStep - 1) / (progressSteps.length - 1)) * 100;
  progressBarFill.style.width = `${progressPercentage}%`;

  // Enable/disable buttons
  prevButton.disabled = currentStep === 1;
  nextButton.disabled = currentStep === progressSteps.length;
  if (currentStep === progressSteps.length) {
    submit.classList.remove('visually-hidden');
  }
  else {
    submit.classList.add('visually-hidden');
  }
}


nextButton.addEventListener("click", () => {
  if (next_page()) {
    if (currentStep < progressSteps.length) {
      currentStep++;
      updateProgress();
    }
  }
});

prevButton.addEventListener("click", () => {
  if (currentStep > 1) {
    currentStep--;
    updateProgress();
  }
  previous_page()
});


// Validation Funtions ********************

function validate_basic_detail() {
  const errorElement = document.getElementById("cmp_frm_err_1");
  errorElement.textContent = ""; // Clear previous error messages

  // Get field values
  const birthDate = document.getElementById("txtDate").value.trim();
  const bio = document.getElementById("exampleFormControlTextarea1").value.trim();
  const genderMale = document.getElementById("male").checked;
  const genderFemale = document.getElementById("female").checked;
  const location = document.getElementById("location").value.trim();

  // Check required fields
  if (!birthDate) {
    errorElement.textContent = "Please enter your birth date.";
    return false;
  }

  if (!bio) {
    errorElement.textContent = "Please enter your bio.";
    return false;
  }

  if (!genderMale && !genderFemale) {
    errorElement.textContent = "Please select your gender.";
    return false;
  }

  if (!location) {
    errorElement.textContent = "Please enter your location.";
    return false;
  }

  errorElement.textContent = ""; // All fields are valid
  return true;
}
function validateEducationForm() {
  let isValid = true; // Flag to track validity
  let hasDegree = false;
  const errorElement = document.querySelector(".error_p"); // Error display element
  const requiredInputs = document.querySelectorAll('#Educaiton input');

  const educationLevel = document.querySelector('input[name="education_level"]:checked'); // Check selected education level
  const schoolMedium = document.getElementById("medium");
  errorElement.classList.remove('visually-hidden')
  // Check if highest education level is selected
  if (!educationLevel) {
    console.log('educationLevel not filled')
    isValid = false;
    errorElement.classList.remove('visually-hidden')
    document.querySelector('input[name="education_level"]').scrollIntoView({ behavior: 'smooth', block: 'center' });
    return isValid;
  }
  // console.log(educationLevel.value)
  const selectedEducation = educationLevel.value; // Get the selected education level value
  // Validate school medium if education level is "10" or "12"

   if (selectedEducation === "diploma") {
    hasDegree = true
    const diploma_degree = document.getElementById('diploma_degree');
    if (diploma_degree.value === "") {
      isValid = false;
      diploma_degree.scrollIntoView({ behavior: 'smooth', block: 'center' });
      errorElement.classList.remove('visually-hidden')
      return isValid
    }
  }
  else if (selectedEducation === "iti") {
    hasDegree = true
    const iti_degree = document.getElementById('iti_degree');
    if (iti_degree.value === "") {
      isValid = false;
      iti_degree.scrollIntoView({ behavior: 'smooth', block: 'center' });
      errorElement.classList.remove('visually-hidden')
      return isValid
    }
  }
  else if (selectedEducation === "graduate") {
    hasDegree = true
    const graduate_degree = document.getElementById('graduateDegree');
    if (graduate_degree.value === "") {
      isValid = false;
      graduate_degree.scrollIntoView({ behavior: 'smooth', block: 'center' });
      errorElement.classList.remove('visually-hidden')
      return isValid
    }
  }
  else if (selectedEducation === "p_graduate") {
    hasDegree = true
    const p_graduate_degree = document.getElementById('postgraduateDegree');
    if (p_graduate_degree.value === "") {
      isValid = false;
      p_graduate_degree.scrollIntoView({ behavior: 'smooth', block: 'center' });
      errorElement.classList.remove('visually-hidden')
      return isValid
    }
  }
 if (hasDegree){
  const Specialization = document.getElementById('Specialization')
  if (Specialization.value === "") {
    isValid = false;
    Specialization.scrollIntoView({ behavior: 'smooth', block: 'center' });
    errorElement.classList.remove('visually-hidden')
    return isValid
  }

  requiredInputs.forEach((inp) => {
    if (inp.value === "") {
      isValid = false;
      errorElement.textContent = 'Please fill the required fields.';
    }
  })
 }

 if (!schoolMedium || !schoolMedium.value.trim()) {
  console.log('medium not filled')
  isValid = false;
  schoolMedium.focus(); // Focus the field
  errorElement.classList.remove('visually-hidden')
  return isValid;
}
  errorElement.classList.add('visually-hidden')
  return isValid; // Return the validity status
}

function validateExperienc(){
  isValid = true
  const experience = document.querySelector('#Experience input[name ="work_experience"]:checked');
  const current_working = document.querySelector('#Experience input[name ="current_working"]:checked');
  const notice_period = document.querySelector('#notice_period input[name ="notice_period"]:checked');
  const error_p = document.querySelector('.error_p');
  const jobTitle = document.getElementById('jobTitle');
  const jobRole = document.getElementById('jobRole');
  const companyName = document.getElementById('companyName');
  const industry = document.getElementById('industry');
  const salary = document.getElementById('numberInput');
  const exp_start_date = document.getElementById('exp_start_date');
  const exp_end_date = document.getElementById('exp_end_date');
  const total_experience_year = document.getElementById('total_experience_year');
  if (!experience) {
    isValid = false
    error_p.classList.remove('visually-hidden');
    return isValid
  }
  if (experience.value === "have_experience"){
      if (jobTitle.value === "" || jobRole.value ==="" || companyName.value === "" || industry.value === "") {
        isValid = false;
        error_p.classList.remove('visually-hidden');
        return isValid
      }
      if (current_working.value === "working"){
        if (!notice_period){
          isValid = false
          error_p.classList.remove('visually-hidden');
          return isValid
        }
      }
      if (salary.value === "" || exp_start_date.value === "" || exp_end_date.value === "" || total_experience_year.value === "") {
        isValid = false
        error_p.classList.remove('visually-hidden');
        return isValid
      }


  }
  error_p.classList.add('visually-hidden')
  return isValid;

}

function validateLanguage(){
  const english = document.querySelector('#Language input[name ="english"]:checked');
  isValid = true
  if (!english) {
    isValid = false
    document.querySelector('.error_p').classList.remove('visually-hidden');
    return isValid
  }
  document.querySelector('.error_p').classList.add('visually-hidden');
  return isValid;
}
function validateJobPrefference(){
  const divs = document.querySelectorAll('#job_prefference div');
  const error_p = document.querySelector('.error_p');
  for (const div of divs) {
    const checkboxes = div.querySelectorAll('input[type="checkbox"]');
    let atLeastOneChecked = false;

    for (const checkbox of checkboxes) {
      if (checkbox.checked) {
        atLeastOneChecked = true;
        break; 
      }
    }

    if (!atLeastOneChecked) {
      error_p.classList.remove('visually-hidden'); 
      return false; 
    } else {
      error_p.classList.add('visually-hidden'); 
    }
  }

  return true; 
}

