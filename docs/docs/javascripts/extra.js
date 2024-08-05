document.addEventListener("DOMContentLoaded", function() {
    const repoLink = document.querySelector('body > header > nav > div.md-header__source > a.md-source');
    if (repoLink) {
        repoLink.setAttribute('target', '_blank');
    }
});