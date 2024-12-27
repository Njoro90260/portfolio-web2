document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.classList.remove('show');
            alert.addEventListener('transitionend', () => alert.remove()); 
        });
    }, 5000); 
});
const canvas = document.getElementById('pitchCanvas');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function drawAbstractShape() {
    const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
    gradient.addColorStop(0, 'rgba(255, 0 , 255, 0.8)');
    gradient.addColorStop(0.5, 'rgba(0, 255, 255, 0.8)');
    gradient.addColorStop(1, 'rgba(255, 255, 0, 0.8)');

    ctx.beginPath();
    ctx.moveTo(canvas.width * 0.3, canvas.height * 0.5);
    ctx.bezierCurveTo(
        canvas.width * 0.2, canvas.height * 0.1,
        canvas.width * 0.8, canvas.height * 0.1,
        canvas.width , 0.7, canvas.height * 0.5
    );
    ctx.bezierCurveTo(
        canvas.width * 0.8, canvas.height * 0.9,
        canvas.width * 0.2, canvas.height * 0.9,
        canvas.width * 0.3, canvas.height * 0.5
    );
    ctx.closepath();

    ctx.fillStyle = gradient;
    ctx.fill();

    ctx.lineWidth = 3;
    ctx.strokeStyle = 'white';
    ctx.stroke();
}

function drawText() {
    ctx.fillStyle = '#fff';
    ctx.font = 'bold 48px Arial';
    ctx.fillText('WELCOME', canvas.width * 0.1, canvas.height * 0.3);
    ctx.fillText('IHICODES', canvas.width * 0.1, canvas.width * 0.1, canvas.height * 0.4);

    ctx.font = '20px Arial';
    ctx.fillText('A personal portfolio from me', canvas.width * 0.1, canvas.height * 0.45);

    ctx.font = '16px Arial';
    ctx.fillText('Ingoude Comapny', canvas.width * 0.1, canvas.height * 0.1);
}

function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    draw();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawAbstractShape();
    drawText();
}

window.addEventListener('resize', resizeCanvas);
draw();