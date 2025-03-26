// Main JavaScript File for AuctionHub

// Navbar Toggle for Mobile
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('nav ul');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('show-menu');
    });
}

// Bid Confirmation Popup
function confirmBid(itemId) {
    const bidAmount = prompt("Enter your bid amount:");
    if (bidAmount) {
        alert(`Your bid of $${bidAmount} has been placed on Item ID: ${itemId}`);
    }
}

// Image Preview for File Upload
const imageInput = document.querySelector('#image-upload');
const imagePreview = document.querySelector('#image-preview');

if (imageInput && imagePreview) {
    imageInput.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function () {
                imagePreview.src = reader.result;
                imagePreview.style.display = 'block';
            }
            reader.readAsDataURL(file);
        }
    });
}

// Countdown Timer for Auction
function startCountdown(duration, display) {
    let timer = duration, minutes, seconds;
    setInterval(() => {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = 0;
            display.textContent = "Auction Ended";
        }
    }, 1000);
}

// Automatic Countdown Start (Attach to each auction timer span)
window.onload = function () {
    const auctionTimers = document.querySelectorAll('.auction-timer');
    auctionTimers.forEach(timer => {
        const timeRemaining = parseInt(timer.dataset.duration);
        if (timeRemaining > 0) {
            startCountdown(timeRemaining, timer);
        }
    });
}
