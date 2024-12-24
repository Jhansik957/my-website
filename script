// Sticky header navigation highlight on scroll
const navLinks = document.querySelectorAll('header nav ul li a');
const sections = document.querySelectorAll('section');

window.addEventListener('scroll', () => {
    let currentPosition = window.scrollY + 100;
    
    sections.forEach((section, index) => {
        if (currentPosition >= section.offsetTop && currentPosition < section.offsetTop + section.offsetHeight) {
            navLinks.forEach(link => link.classList.remove('active'));
            navLinks[index].classList.add('active');
        }
    });
});

// Form validation
document.querySelector('form').addEventListener('submit', function(event) {
    const inputs = this.querySelectorAll('input, textarea, select');
    let isValid = true;
    
    inputs.forEach(input => {
        if (input.required && !input.value.trim()) {
            isValid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#ccc';
        }
    });

    if (!isValid) {
        event.preventDefault();
        alert('Please fill out all required fields.');
    }
});

// Toggle collaboration tools section visibility
const toggleButton = document.querySelector('#collaboration-tools button');

toggleButton.addEventListener('click', () => {
    const toolsSection = document.querySelector('#collaboration-tools');
    toolsSection.classList.toggle('hidden');
});

// Adding 'hidden' class in CSS to hide the collaboration tools section initially
const style = document.createElement('style');
style.innerHTML = `
    #collaboration-tools.hidden {
        display: none;
    }
`;
document.head.appendChild(style);
