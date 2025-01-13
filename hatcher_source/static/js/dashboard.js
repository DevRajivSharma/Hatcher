document.getElementById('reload').addEventListener('click', function () {
    location.reload();
  });

document.getElementById('toggle_profile_box').addEventListener('click', (event) => {
document.querySelector('.profile_box').classList.toggle('visually-hidden');
document.querySelector('.profile_dropdown').classList.toggle('rotate-180deg');
});

document.addEventListener('click', (event) => {
    const profileBox = document.querySelector('.profile_box');
    const toggleButton = document.getElementById('toggle_profile_box');
    if (!profileBox.contains(event.target) && !toggleButton.contains(event.target)) {
        profileBox.classList.add('visually-hidden');
        document.querySelector('.profile_dropdown').classList.add('rotate-180deg');
    }
});
