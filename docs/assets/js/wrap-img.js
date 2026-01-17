document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("img").forEach(function (img) {
    // Не трогать, если уже внутри <a>
    if (img.closest("a")) return;

    // Создаём ссылку с href = src изображения
    const link = document.createElement("a");
    link.href = img.src;

    // Lightbox (если используешь)
    link.setAttribute("data-lightbox", "gallery");
    link.setAttribute("data-title", img.alt || "");

    // Опционально: открыть в новой вкладке
    // link.setAttribute("target", "_blank");

    // Оборачиваем
    img.parentNode.insertBefore(link, img);
    link.appendChild(img);
  });
});
