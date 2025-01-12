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