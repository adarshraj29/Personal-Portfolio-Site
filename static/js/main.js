const menuToggle = document.querySelector('#menuToggle');
const navLinks = document.querySelector('#navLinks');
if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => {
    const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', String(!expanded));
    navLinks.classList.toggle('nav-open');
  });
  navLinks.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    navLinks.classList.remove('nav-open');
    menuToggle.setAttribute('aria-expanded', 'false');
  }));
}
