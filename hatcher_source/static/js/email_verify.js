function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}

document.getElementById('send-otp-btn').addEventListener('click', () => {
    const email = document.getElementById('email').value;
    if (!email) {
        alert('Please enter an email');
        return;
    }
    const e_spin = document.getElementById('e-spin')
    const sd_otp = document.getElementById('sd-otp')
    e_spin.classList.remove('visually-hidden')
    sd_otp.classList.add('visually-hidden')
    fetch('/email-auth/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCSRFToken(),
        },
        body: `email=${encodeURIComponent(email)}`
    })
    .then(response => response.json())
    .then(data => {
        e_spin.classList.add('visually-hidden')
        sd_otp.classList.remove('visually-hidden')
        alert(data.message)
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('verify-otp-btn').addEventListener('click', () => {
    const otp = document.getElementById('otp').value;
    if (!otp) {
        alert('Please enter an otp');
        return;
    }
    const o_spin = document.getElementById('o-spin')
    const v_otp = document.getElementById('v-otp')
    o_spin.classList.remove('visually-hidden')
    v_otp.classList.add('visually-hidden')
    fetch('/verify-otp/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCSRFToken(),
         },
        body: `otp=${encodeURIComponent(otp)}`
    })
    .then(response => response.json())
    .then(data => {
        o_spin.classList.add('visually-hidden')
        v_otp.classList.remove('visually-hidden')
        alert(data.message)
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('submit-btn').addEventListener('click', function (e) {
    const password = document.getElementById('Password').value;
    const confirmPassword = document.getElementById('Password2').value;

    if (password !== confirmPassword) {
        e.preventDefault(); // Prevent form submission
        alert("Passwords do not match!");
    }
});