document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.wrapper, img, .text-box, .navbar, .btn');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    });
    elements.forEach(el => observer.observe(el));
})