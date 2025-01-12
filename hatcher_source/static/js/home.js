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

