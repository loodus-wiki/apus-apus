document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', function() {
        const button = document.getElementById('back-to-top');
        if (button) { // Проверка на null
            if (document.body.scrollTop > 600 || document.documentElement.scrollTop > 600) {
                button.style.display = 'block';
            } else {
                button.style.display = 'none';
            }
        }
    });

    // Делаем scrollToTop глобальной функцией, чтобы она была доступна для onclick
    window.scrollToTop = function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };
});
