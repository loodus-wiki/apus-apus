---
layout: default
title: Правильное кормление стрижа
lang: ru
is_home: false
---

<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{PAGE_TITLE}}</title>
    <meta name="description" content="О стрижах">
    <link rel="stylesheet" href="../assets/css/styles.css">

    <!-- hreflang для SEO -->
    <link rel="alternate" hreflang="ru" href="../ru/{{PAGE_PATH}}">
    <link rel="alternate" hreflang="en" href="../en/{{PAGE_PATH}}">
    <link rel="alternate" hreflang="est" href="../est/{{PAGE_PATH}}">
    <link rel="alternate" hreflang="x-default" href="../{{PAGE_PATH}}">
</head>

<body>
    <!-- Переключатель языков -->
    <div class="language-switcher">
        <a href="../ru/{{PAGE_PATH}}" {{RU_ACTIVE}}>RU</a>
        <a href="../en/{{PAGE_PATH}}" {{EN_ACTIVE}}>EN</a>
        <a href="../est/{{PAGE_PATH}}" {{EST_ACTIVE}}>EST</a>
    </div>

    <!-- Навигация -->
    <header>
        <nav>
            <ul>
                {% for item in site.data.navigation-ru %}
                <li><a href="{{ item.url | relative_url }}">{{ item.title }}</a></li>
                {% endfor %}
            </ul>
        </nav>
    </header>

    <!-- Основной контент -->
    <main id="t-main-content">
        {{MAIN_CONTENT}}

        Давайте убедимся, что Вы нашли именно стрижа, а не ласточку или коршуна.

Небольшая птица, размером с ладонь, темно-бурого практически однотонного окраса с темно-карими глазками бусинками. Все четыре пальца на каждой лапке направлены вперед, имеют длинные острые коготки. Крылья длинные, саблевидные (серповидные), выступают за хвост примерно на 3,5 сантиметра.


<img src="/apus-apus/assets/images/adult_swift.webp" alt="Adult Swift">

Время
Если вы нашли своего стрижа в мае или июне, то это совершенно точно взрослый стриж. В это время еще нет птенцов.

Именно так выглядит взрослый стриж.
А птенец?


    </main>

    <script src="../assets/js/language-switcher.js"></script>
</body>

</html>