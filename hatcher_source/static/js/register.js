function getCSRFToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}


const submit_btn = document.getElementById('submit-btn');
submit_btn.addEventListener('click', (event) => {

    event.preventDefault();
    // Get password and confirm password values
    const errorMessage = document.getElementById('error-message');
    const details_group = document.querySelector('.details-group');
    let errorMessages = [];
    let isValid = true;
    const password = document.getElementById('Password').value.trim();
    const confirmPassword = document.getElementById('Confirm_Password').value.trim();
    if (!confirmPassword) {
        isValid = false;
        errorMessages = 'Confirm Password is required.';
    } else if (password !== confirmPassword) {
        isValid = false;
        errorMessages = 'Passwords do not match.';
    }

    if (!password) {
        isValid = false;
        errorMessages = 'Password is required.';
    } else if (password.length < 8) {
        isValid = false;
        errorMessages = 'Password must be at least 8 characters long.';
    }

    const email = document.getElementById('Email').value.trim();
    if (!email) {
        isValid = false;
        errorMessages = 'Email is required.';
    } else if (!/^\S+@\S+\.\S+$/.test(email)) {
        isValid = false;
        errorMessages = 'Email format is invalid.';
    }

    const lastName = document.getElementById('LastName').value.trim();
    if (!lastName) {
        isValid = false;
        errorMessages = 'Last Name is required.';
    }

    const firstName = document.getElementById('FirstName').value.trim();
    if (!firstName) {
        isValid = false;
        errorMessages = 'First Name is required.';
    }

    // Display error messages or proceed
    if (!isValid) {
        errorMessage.innerHTML = errorMessages; // Display errors
        return false;
    }
    console.log(errorMessages);
    // Clear any previous error messages
    errorMessage.textContent = '';
    
    // Check if passwords match
    if (password !== confirmPassword) {
        errorMessage.textContent = 'Passwords do not match. Please try again.';
        return false; // Prevent form submission
    }
    // Proceed with form submission
    submit_btn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
    const otp_email = document.getElementById('otp-email');
    otp_email.textContent = email;
    // details_group.classList.add('visually-hidden');
    // const otp_section = document.getElementById('otp-section');
    // otp_section.classList.remove('visually-hidden'); // Make OTP input visible
    // submit_btn.classList.add('visually-hidden');
    const b_line = document.getElementById('break')
    fetch('/email-auth/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCSRFToken(),
        },
        body: `email=${encodeURIComponent(email)}&type=user`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Show OTP verification fields
            details_group.classList.add('visually-hidden');
            const otp_section = document.getElementById('otp-section');
            otp_section.classList.remove('visually-hidden'); // Make OTP input visible
            submit_btn.classList.add('visually-hidden');
            b_line.classList.add('hidden')
            // Wait for the OTP input and verify after the user enters it
            const verifyOtpBtn = document.getElementById('verify-otp-btn');
            verifyOtpBtn.addEventListener('click', () => {
                const otp_val1 = document.getElementById('otp_val1').value;
                const otp_val2 = document.getElementById('otp_val2').value;
                const otp_val3 = document.getElementById('otp_val3').value;
                const otp_val4 = document.getElementById('otp_val4').value;
                const otp = otp_val1 + otp_val2 + otp_val3 + otp_val4;

                // Check if OTP is complete
                if (otp.length !== 4) {
                    errorMessage.textContent = 'Please enter all 4 digits of OTP.';
                    return false;
                }

                fetch('/verify-otp/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': getCSRFToken(),
                    },
                    body: `otp=${encodeURIComponent(otp)}`
                })
                .then(response => response.json())
                .then(data => {
                    // Handle OTP verification response
                    if (data.status === 'success') {
                        // OTP verified successfully, now submit the form
                        // Submit the form programmatically after successful OTP verification
                        const form = document.getElementById('register-form');
                        form.submit();  // This submits the form

                    } else {
                        // OTP is incorrect
                        errorMessage.textContent = 'Invalid OTP. Please try again.';
                    }
                })
                .catch(error => {
                    console.error('Error during OTP verification:', error);
                    errorMessage.textContent = 'An error occurred while verifying OTP. Please try again.';
                });
            });
        } else {
            errorMessage.textContent = data.message;
            submit_btn.innerHTML = 'Register';
        }
    })
    .catch(error => {
        errorMessage.textContent=
        errorMessage.textContent = 'An error occurred. Please try again.';
    });

    return false; // Prevent form submission while OTP is being sent and verified
});

// Move focus to next input when a value is entered
document.querySelectorAll('.otp-input').forEach((input, index, inputs) => {
    // Automatically move to next input when a value is entered
    input.addEventListener('input', function() {
        // If the input has value, move focus to the next input
        if (this.value.length === 1 && index < inputs.length - 1) {
            inputs[index + 1].focus();
        }
    });

    // Move to previous input if backspace is pressed
    input.addEventListener('keydown', function(event) {
        if (event.key === 'Backspace' && this.value === '') {
            if (index > 0) {
                inputs[index - 1].focus();
            }
        }
    });
});

const show_pass = document.getElementById('show_pass');
const hide_pass = document.getElementById('hide_pass');
const show_confirm_pass = document.getElementById('show_confirm_pass');
const hide_confirm_pass = document.getElementById('hide_confirm_pass');

show_pass.addEventListener('click', () => {
    const password = document.getElementById('Password');
    password.type = 'password';
    show_pass.classList.add('visually-hidden');
    hide_pass.classList.remove('visually-hidden');
});
hide_pass.addEventListener('click', () => {
    const password = document.getElementById('Password');
    password.type = 'text';
    hide_pass.classList.add('visually-hidden');
    show_pass.classList.remove('visually-hidden');
});
show_confirm_pass.addEventListener('click', () => {
    const confirm_password = document.getElementById('Confirm_Password');
    confirm_password.type = 'password';
    show_confirm_pass.classList.add('visually-hidden');
    hide_confirm_pass.classList.remove('visually-hidden');
});
hide_confirm_pass.addEventListener('click', () => {
    const confirm_password = document.getElementById('Confirm_Password');
    confirm_password.type = 'text';
    hide_confirm_pass.classList.add('visually-hidden');
    show_confirm_pass.classList.remove('visually-hidden');
});