document.addEventListener('DOMContentLoaded', () => {
    // Auto-scroll to contact section if URL contains #contact
    if (window.location.hash === "#contact") {
        const contactSection = document.querySelector("#contact");
        contactSection.scrollIntoView({ behavior: "smooth" });
    }

    // Real-time character counter for the message field
    const messageField = document.querySelector("[name='message']");
    if (messageField) {
        const charCount = document.createElement("small");
        charCount.style.display = "block";
        charCount.style.textAlign = "right";
        charCount.style.color = "var(--text-color2)";
        messageField.parentNode.appendChild(charCount);

        messageField.addEventListener("input", function () {
            charCount.textContent = `${messageField.value.length}/500 characters`;
            if (messageField.value.length > 500) {
                charCount.style.color = "red";
            } else {
                charCount.style.color = "var(--text-color2)";
            }
        });
    }
    // Smooth scroll
    const links = document.querySelectorAll('nav ul li a');
    links.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 50,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Alerts
    setTimeout(() => {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.classList.remove('show');
            alert.addEventListener('transitionend', () => alert.remove());
        });
    }, 5000);

    // Canvas Animation
    const canvas = document.getElementById('pitchCanvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const stars = [];
        const numStars = 100;

        const randomColor = () => {
            const colors = [
                '#FFF', '#f3f3f3', '#1e0e3e', '#02022e', '#7645d8', '#02022eac', '#ffffff80'
            ];
            return colors[Math.floor(Math.random() * colors.length)];
        };

        const createStar = () => ({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 3 + 1,
            color: randomColor(),
            dx: (Math.random() - 0.5) * 2,
            dy: (Math.random() - 0.5) * 2
        });

        for (let i = 0; i < numStars; i++) {
            stars.push(createStar());
        }

        const drawStar = star => {
            ctx.beginPath();
            ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
            ctx.fillStyle = star.color;
            ctx.fill();
            ctx.closePath();
        };

        const animate = () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            stars.forEach(star => {
                star.x += star.dx;
                star.y += star.dy;

                if (star.x < 0 || star.x > canvas.width) star.dx *= -1;
                if (star.y < 0 || star.y > canvas.height) star.dy *= -1;

                drawStar(star);
            });

            requestAnimationFrame(animate);
        };

        animate();

        const debounceResize = (func, delay) => {
            let timeout;
            return () => {
                clearTimeout(timeout);
                timeout = setTimeout(func, delay);
            };
        };

        window.addEventListener(
            'resize',
            debounceResize(() => {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }, 200)
        );
    }

    // Intersection Observer for Animations
    const projectContainers = document.querySelectorAll('.project-container');
    if (projectContainers.length) {
        const observer = new IntersectionObserver(
            entries => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-fade-in');
                    }
                });
            },
            { threshold: 0.2 }
        );

        projectContainers.forEach(container => observer.observe(container));
    }
    function hoverButtonEffect(button) {
        button.style.backgroundColor = '#7645d8'; // Custom theme color
        button.style.color = '#fff';
    }

    function resetButtonEffect(button) {
        button.style.backgroundColor = ''; // Reset to default
        button.style.color = '';
    }

    // Smooth scrolling on page load
    const projectTitle = document.querySelector('h1');
    projectTitle.scrollIntoView({
        behavior: 'smooth',
        block: 'center'
    });
});
