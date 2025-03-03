function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function applyRandomColor() {
    const element = document.getElementById('colorful-element');
    element.style.backgroundColor = getRandomColor();
}

// Call the function to apply a random color when the page loads
window.onload = applyRandomColor;
