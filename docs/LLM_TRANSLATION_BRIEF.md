# LLM TRANSLATION BRIEF — Инструкция для LLM-переводчика

> Прочитайте этот файл перед началом работы с переводами.

---

## Проект

Jekyll GitHub Pages — энциклопедия по реабилитации стрижей (Apus apus).

- **URL:** https://loodus-wiki.github.io/apus-apus/
- **Репозиторий:** `C:\Users\User\Documents\swift_apus-apus\gitpages\docs\`
- **Источник правды:** `ru/` — все переводы делаются с русских файлов.

---

## Структура front matter

Каждый файл начинается с:

```yaml
---
layout: default
title: Заголовок на языке страницы
lang: ru          # или est, ua
is_home: false    # true только для index.md и страниц без header
description: Краткое описание (~155 символов) для SEO
---
```

Для страниц без перевода (региональный контент):
```yaml
no_translate: true
```

---

## Правила перевода

1. **Только содержание** — front matter переводить, структура HTML сохраняется
2. **alt-тексты** изображений переводить на язык страницы
3. **Ссылки** внутри сайта: `feeding-swift.html`, `exhaustion.html` — имена файлов не меняются
4. **Числа, дозировки, таблицы** — числа не переводить, только подписи
5. **Предупреждения** — не смягчать: «категорически нельзя» → «категорично заборонено» / «kategooriliselt keelatud»
6. **Видео:** общие файлы — путь без суффикса; локализованные — добавить `<!-- media:localized -->`

## Чего НЕ делать

- ❌ Не добавлять `<head>` в markdown — layout уже содержит `<head>`
- ❌ Не переводить `_drafts.md`, `_emergency.md`, `cure-swift.md`
- ❌ Не использовать `ritsikad` вместо `kilgid` (EST)
- ❌ Не использовать `prussakad` без уточнения «söödavad marmorprussakad» (EST)
- ❌ Не переводить `more-information.md` — маркер `no_translate: true`

---

## Полный глоссарий

→ См. `TRANSLATION_GUIDE.md` в корне docs/

## Таблица лекарств

→ См. `MEDICATIONS_TABLE.md` в корне docs/

---

## Контакты для UA-раздела

```markdown
- [Стрижі: інформація та допомога](https://www.facebook.com/groups/swifts.information/) (Дніпро)
- [Їс рук в небо!](https://www.facebook.com/groups/is.ruk.v.nebo/) (Дніпро)
- [«Вільні крила»](https://www.instagram.com/freewingslviv/) — Центр реабілітації (Львів)
- [Центри реабілітації (WWF Україна)](https://wwf.ua/?311751%2Fwild-animals-what-to-do=)
```

## Медиа-конвенция

```
assets/images/fethers-count-ru.png   ← с текстом на RU
assets/images/fethers-count-est.png  ← с текстом на EST
assets/video/feeding-adult-swift2-ru.mp4   ← с озвучкой RU
assets/video/feeding-adult-swift1.mp4      ← общее, без озвучки
```

Комментарии в markdown:
```html
<!-- media:localized — есть версия на языке страницы -->
<!-- media:pending-localization — нужна локализация, пока общая -->
```