// Автоматическое определение языка браузера
function detectBrowserLanguage() {
    const browserLang = navigator.language || navigator.userLanguage;
    const supportedLangs = ['ru', 'en', 'est'];
    const langCode = browserLang.substring(0, 2);
    
    if (supportedLangs.includes(langCode)) {
        return langCode;
    }
    return 'en'; // fallback
}

// Перенаправление на нужную языковую версию
function redirectToLanguage() {
    const currentPath = window.location.pathname;
    const baseURL = window.location.origin + window.location.pathname.split('/docs')[0];
    
    // Если находимся на главной странице /docs/ или /docs/index.html
    if (currentPath.endsWith('/docs/') || currentPath.endsWith('/docs/index.html') || currentPath.endsWith('/docs')) {
        const detectedLang = detectBrowserLanguage();
        const hasVisited = localStorage.getItem('swift-site-language');
        
        if (!hasVisited) {
            //  Относительный путь для папки /docs
            window.location.href = `${detectedLang}/`;
            localStorage.setItem('swift-site-language', detectedLang);
        }
    }
}

// Запуск при загрузке страницы
document.addEventListener('DOMContentLoaded', redirectToLanguage);