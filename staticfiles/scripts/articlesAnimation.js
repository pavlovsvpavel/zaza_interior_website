document.addEventListener("DOMContentLoaded", () => {
    const articles = document.querySelectorAll("#articles-section article");

    articles.forEach((article, index) => {
        setTimeout(() => {
            article.classList.add("article-visible");
        }, index * 300);
    });
});