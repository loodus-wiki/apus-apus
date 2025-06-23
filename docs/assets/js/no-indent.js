document.addEventListener('DOMContentLoaded', () => {
  const paragraphs = document.querySelectorAll('p');
  paragraphs.forEach(p => {
    if (p.textContent.length < 85) { // Порог для "короткого" текста
      p.classList.add('no-indent');
    }
  });
});