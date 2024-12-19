document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll("#nav-menu .links-container .nav-link");
    const currentPath = window.location.pathname;

    // Set active class based on current URL
    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }

        // Add click event for user navigation
        link.addEventListener("click", function() {
            // Remove active from all links
            navLinks.forEach(link => link.classList.remove("active"));
            // Add active class to the clicked link
            this.classList.add("active");
        });
    });
});


