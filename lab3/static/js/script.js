document.addEventListener('DOMContentLoaded', function() {
    // Отримуємо URL поточної сторінки
    var currentUrl = window.location.href;

    // Отримуємо всі посилання в навігаційному меню
    var navLinks = document.querySelectorAll('.navbar-nav .nav-item a');

    // Ітеруємося по кожному посиланні
    navLinks.forEach(function(link) {
        // Перевіряємо, чи посилання відповідає поточній сторінці
        if (link.href === currentUrl) {
            // Додаємо клас "active" до батьківського елементу (li)
            link.parentElement.classList.add('active');
        }
    });
});