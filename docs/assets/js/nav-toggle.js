document.addEventListener('DOMContentLoaded', () => {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');

    // Обработчик для мобильного меню (гамбургер)
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
        if (pathParts.length > 1 && pathParts[0] === baseUrl.replace('/', '') && ['ru', 'est', 'ua', 'en'].includes(pathParts[1])) {
            // Заменяем языковой код, сохраняя baseurl
            pathParts[1] = newLang;
            newPath = `/${pathParts.join('/')}`;
        } else if (pathParts.length > 0 && ['ru', 'est', 'ua', 'en'].includes(pathParts[0])) {
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

    // Dropdown: открытие/закрытие по клику на триггер
    document.querySelectorAll('.lang-dropdown-trigger').forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const dropdown = trigger.closest('.lang-dropdown');
            if (!dropdown) return;
            const isOpen = dropdown.classList.contains('open');
            // Закрыть все открытые дропдауны
            document.querySelectorAll('.lang-dropdown.open').forEach(dd => {
                dd.classList.remove('open');
                dd.querySelector('.lang-dropdown-trigger')?.setAttribute('aria-expanded', 'false');
            });
            // Открыть текущий (если был закрыт)
            if (!isOpen) {
                dropdown.classList.add('open');
                trigger.setAttribute('aria-expanded', 'true');
            }
        });
    });

    // Переключение языка по клику на пункт меню
    document.querySelectorAll('.lang-switch-option').forEach(option => {
        option.addEventListener('click', (e) => {
            e.preventDefault();
            const newLang = option.getAttribute('data-lang');
            if (newLang) switchToSamePage(newLang);
        });
    });

    // Закрыть дропдаун при клике вне него
    document.addEventListener('click', (e) => {
        document.querySelectorAll('.lang-dropdown.open').forEach(dd => {
            if (!dd.contains(e.target)) {
                dd.classList.remove('open');
                dd.querySelector('.lang-dropdown-trigger')?.setAttribute('aria-expanded', 'false');
            }
        });
    });

    // Закрыть дропдаун при нажатии Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            document.querySelectorAll('.lang-dropdown.open').forEach(dd => {
                dd.classList.remove('open');
                dd.querySelector('.lang-dropdown-trigger')?.setAttribute('aria-expanded', 'false');
            });
        }
    });
});