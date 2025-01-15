function resizePage() {
    const width = window.innerWidth;

    // Condition for screen width greater than 1470px (default scale of 100%)
    if (width > 1470) {
        document.body.style.transform = 'scale(1)';
        document.body.style.transformOrigin = 'top left';
    }
    // Condition a: If the screen width is between 992px and 1600px, shrink the page by 90%
    else if (width >= 992 && width <= 1600) {
        document.body.style.transform = 'scale(0.9)';
        document.body.style.transformOrigin = 'top left';
    }
    // Condition b: If the screen width is between 700px and 767px, shrink the page by 80%
    else if (width >= 700 && width <= 767) {
        document.body.style.transform = 'scale(0.8)';
        document.body.style.transformOrigin = 'top left';
    }
    // Condition c: If the screen width is between 600px and 700px, shrink the width to 75%
    else if (width >= 600 && width <= 700) {
        document.body.style.transform = 'scale(0.75)';
        document.body.style.transformOrigin = 'top left';
    }
    // Condition d: If the screen width is less than or equal to 600px, shrink the width to 50%
    else if (width <= 600) {
        document.body.style.transform = 'scale(0.5)';
        document.body.style.transformOrigin = 'top left';
    }
    // Reset transform if width is greater than 1600px or any other default condition
    else {
        document.body.style.transform = 'scale(1)';
    }
}

// Add event listener to adjust page size when window is resized
window.addEventListener('resize', resizePage);

// Call resizePage initially to apply the correct scale when the page loads
resizePage();
