let page = 1;
let loading = false;
let images = [];

const modal = document.getElementById("myModal");
const modalImg = document.getElementById("fullImage");
const imageName = document.getElementById("imageName");
const imageDescription = document.getElementById("imageDescription");

// Load images dynamically via AJAX
function loadImages() {
    if (loading) return;
    loading = true;
    document.getElementById('loading').style.display = 'block';

    fetch(`/load-images/?page=${page}`)
        .then(response => response.json())
        .then(data => {
            data.images.forEach((image, index) => {
                let li = document.createElement('li');
                li.classList.add('image-card');

                // Create thumbnail image element
                let imgElement = document.createElement('img');
                imgElement.src = image.thumbnail_url;
                imgElement.alt = image.alt;

                // Capture the current length of the images array before pushing the new image
                let currentIndex = images.length;

                // Set the correct index for the onclick event
                imgElement.onclick = function () {
                    openModal(currentIndex);
                };

                // Create description paragraph (alt text)
                let pElement = document.createElement('p');
                pElement.textContent = image.alt || 'No name';

                // Append elements to the list item
                li.appendChild(imgElement);
                li.appendChild(pElement);
                document.getElementById('gallery').appendChild(li);

                // Add full-size image URL to the array for modal
                images.push({
                    url: image.full_size_url,
                    alt: image.alt,
                    description: image.description
                });
            });

            loading = false;
            document.getElementById('loading').style.display = 'none';

            if (data.has_next) {
                page += 1;
            } else {
                window.removeEventListener('scroll', onScroll);
            }
        });
}

// Scroll event to load more images when reaching the bottom of the page
function onScroll() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 500) {
        loadImages();
    }
}

window.addEventListener('scroll', onScroll);

loadImages();

let currentIndex = 0;

// --- Keyboard Navigation Handler ---
function handleKeyDown(event) {
    if (modal.style.display !== "flex") return;

    switch (event.key) {
        case "ArrowLeft":
            previousImage();
            break;
        case "ArrowRight":
            nextImage();
            break;
        case "Escape":
            closeModal();
            break;
    }
}

// --- Swipe Navigation Handlers ---
let touchstartX = 0;
const swipeThreshold = 50;

function handleTouchStart(event) {
    touchstartX = event.changedTouches[0].screenX;
}

function handleTouchEnd(event) {
    if (images.length === 0) return;
    const touchendX = event.changedTouches[0].screenX;
    const swipeDistance = touchendX - touchstartX;

    if (swipeDistance < -swipeThreshold) {
        nextImage();
    } else if (swipeDistance > swipeThreshold) {
        previousImage();
    }
}

// Function to open the modal with the full-size image
function openModal(index) {
    currentIndex = index;
    modal.style.display = "flex";
    if (images[currentIndex]) {
        modalImg.src = images[currentIndex].url;
        imageName.textContent = images[currentIndex].alt;
        imageDescription.textContent = images[currentIndex].description;
    } else {
        console.error("Full-size image URL is undefined for index: ", currentIndex);
    }


    // Event listeners for keyboard and swipe
    document.addEventListener('keydown', handleKeyDown);
    modalImg.addEventListener('touchstart', handleTouchStart, {passive: true});
    modalImg.addEventListener('touchend', handleTouchEnd, {passive: true});
}

// Function to close the modal
function closeModal() {
    modal.style.display = "none";
}

// Function to navigate to the previous image in the modal
function previousImage() {
    currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
    modalImg.src = images[currentIndex].url;
    imageName.textContent = images[currentIndex].alt;
    imageDescription.textContent = images[currentIndex].description;
}

// Function to navigate to the next image in the modal
function nextImage() {
    currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
    modalImg.src = images[currentIndex].url;
    imageName.textContent = images[currentIndex].alt;
    imageDescription.textContent = images[currentIndex].description;
}

