const images = [
    'images/image1.jpg',
    'images/image2.jpg',
    'images/image3.jpg',
    'images/image4.jpg',
    'images/image5.jpg'
];

let currentIndex = 0;

const sliderImage = document.getElementById('slider-image');
const imageCounter = document.getElementById('image-counter');

document.getElementById('next').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    updateSlider();
});

document.getElementById('prev').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateSlider();
});

function updateSlider() {
    sliderImage.src = images[currentIndex];
    imageCounter.textContent = `Слайд ${currentIndex + 1} из ${images.length}`;
}

updateSlider();
