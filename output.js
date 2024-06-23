document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for internal links
    const links = document.querySelectorAll('a[href^="#"]');
    for (const link of links) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    }
    
    // Hover effect for navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    for (const navLink of navLinks) {
        navLink.addEventListener('mouseenter', function () {
            this.style.color = '#000000';
        });
        navLink.addEventListener('mouseleave', function () {
            this.style.color = '#FFFFFF';
        });
    }
});