function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}

async function send_otp() {
    const email = document.getElementById('Email').value;
    const otp_email = document.getElementById('otp-email');
    otp_email.textContent = email;
    const errorMessage = document.getElementById('error-message');
    const details_group = document.getElementById('details-group');
    await fetch('/email-auth/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCSRFToken(),
        },
        body: `email=${encodeURIComponent(email)}`
    })
    .then(response => response.json())
    .then(data => {
        if(data.status === 'success') {
            details_group.classList.add('visually-hidden');
        }
        else {
        errorMessage.textContent = data.message;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        errorMessage.textContent = 'An error occurred. Please try again.';
    });
};

async function verify_otp() {
    const otp_val1 = document.getElementById('otp_val1').value;
    const otp_val2 = document.getElementById('otp_val2').value;
    const otp_val3 = document.getElementById('otp_val3').value;
    const otp_val4 = document.getElementById('otp_val4').value;
    otp = otp_val1 + otp_val2 + otp_val3 + otp_val4;
    await fetch('/verify-otp/', {
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
};