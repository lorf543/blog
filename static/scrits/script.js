const menuButton = document.getElementById('menu-button');

const menuClose = document.getElementById('menuClose');

const submenu = document.getElementById('submenu');

menuButton.addEventListener('click', () => {
  submenu.classList.toggle('hidden');
});

menuClose.addEventListener('click', () => {
  submenu.classList.remove('hidden');
});