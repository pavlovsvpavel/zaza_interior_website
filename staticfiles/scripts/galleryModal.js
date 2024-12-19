let page = 1;
let loading = false;
let images = [];

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
                imgElement.src = image.thumbnail_url;  // Thumbnail URL
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
                window.removeEventListener('scroll', onScroll);  // No more pages to load
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

// Initial load
loadImages();

// Modal functionality for full-size image display
let currentIndex = 0;

// Function to open the modal with the full-size image
function openModal(index) {
    currentIndex = index;
    const modal = document.getElementById("myModal");
    const modalImg = document.getElementById("fullImage");
    const imageName = document.getElementById("imageName");
    const imageDescription = document.getElementById("imageDescription");
    modal.style.display = "flex";
    if (images[currentIndex]) {
        // Set the full-size image
        modalImg.src = images[currentIndex].url;
        // Set the image name and description
        imageName.textContent = images[currentIndex].alt;
        imageDescription.textContent = images[currentIndex].description;
    } else {
        console.error("Full-size image URL is undefined for index: ", currentIndex);
    }
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById("myModal");
    modal.style.display = "none";
}

// Function to navigate to the previous image in the modal
function previousImage() {
    currentIndex = (currentIndex === 0) ? images.length - 1 : currentIndex - 1;
    document.getElementById("fullImage").src = images[currentIndex].url;
    document.getElementById("imageName").textContent = images[currentIndex].alt;
    document.getElementById("imageDescription").textContent = images[currentIndex].description;
}

// Function to navigate to the next image in the modal
function nextImage() {
    currentIndex = (currentIndex === images.length - 1) ? 0 : currentIndex + 1;
    document.getElementById("fullImage").src = images[currentIndex].url;
    document.getElementById("imageName").textContent = images[currentIndex].alt;
    document.getElementById("imageDescription").textContent = images[currentIndex].description;
}

// Close the modal when clicking outside the image
window.onclick = function (event) {
    const modal = document.getElementById("myModal");
    if (event.target === modal) {
        closeModal();
    }
}
