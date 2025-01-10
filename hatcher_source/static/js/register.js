function validatedetails() {
    // Get password and confirm password values
    const password = document.getElementById('Password').value;
    const confirmPassword = document.getElementById('Confirm_Password').value;
    const errorMessage = document.getElementById('error-message');

    // Clear any previous error messages
    errorMessage.textContent = '';

    // Check if passwords match
    if (password !== confirmPassword) {
      errorMessage.textContent = 'Passwords do not match. Please try again.';
      return false; // Prevent form submission
    }

    return true; // Allow form submission
  }