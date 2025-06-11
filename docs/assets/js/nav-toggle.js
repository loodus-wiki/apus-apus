document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    // Обработчик для мобильного меню
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('active');
        });
    }

    function switchToSamePage(newLang) {
        const currentPath = window.location.pathname;
        const queryString = window.location.search;
        const hash = window.location.hash;

        // Базовый путь из _config.yml
        const baseUrl = '/apus-apus';

        // Разбиваем путь на части, убирая пустые элементы
        const pathParts = currentPath.split('/').filter(part => part);

        let newPath;
        // Проверяем, есть ли baseurl и языковой код
        if (pathParts.length > 1 && pathParts[0] === baseUrl.replace('/', '') && ['ru', 'est', 'en'].includes(pathParts[1])) {
            // Заменяем языковой код, сохраняя baseurl
            pathParts[1] = newLang;
            newPath = `/${pathParts.join('/')}`;
        } else if (pathParts.length > 0 && ['ru', 'est', 'en'].includes(pathParts[0])) {
            // Если baseurl отсутствует, но есть языковой код
            pathParts[0] = newLang;
            newPath = `${baseUrl}/${pathParts.join('/')}`;
        } else {
            // Если нет ни языкового кода, ни baseurl
            newPath = `${baseUrl}/${newLang}${currentPath === '/' ? '' : currentPath}`;
        }

        // Формируем полный URL
        window.location.href = newPath + queryString + hash;
    }

    // Обработчики для языковых кнопок
    document.querySelectorAll('.lang-switch').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const newLang = link.classList.contains('lang-est') ? 'est' :
                           link.classList.contains('lang-en') ? 'en' :
                           link.classList.contains('lang-ru') ? 'ru' : null;
            if (newLang) {
                switchToSamePage(newLang);
            }
        });
    });
});