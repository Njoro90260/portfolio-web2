document.getElementById('submit-testimonial').addEventListener('click', function () {
    const form = document.getElementById('testimonial-form');
    const formData = new FormData(form);

    fetch("% url 'add_testimonial' %", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": "{{ csrf_token }}"
        },
    })
        .then(response => response.json())
        .then(data => {
            const messageDiv = document.getElementById('response-message');
            messageDiv.textContent = data.message;
            messageDiv.style.color = data.status === 'success' ? 'green' : 'red';
        })
        .catch(error => {
            console.error('Error:', error);
        });
});