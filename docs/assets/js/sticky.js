document.addEventListener('DOMContentLoaded', function () {
  const navMenu = document.getElementById('nav-menu');
  const stickyNav = document.getElementById('sticky-nav');

  if (navMenu && stickyNav) {
    window.addEventListener('scroll', function () {
      const navMenuRect = navMenu.getBoundingClientRect();
      // Если меню ушло за верхнюю границу экрана
      if (navMenuRect.bottom < 0) {
        stickyNav.style.display = 'flex'; // Показываем фиксированную навигацию
      } else {
        stickyNav.style.display = 'none'; // Скрываем фиксированную навигацию
      }
    });
  }
});