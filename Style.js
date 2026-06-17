const buttons = document.querySelectorAll(".filter-buttons button");
const images = document.querySelectorAll(".gallery .image");

buttons.forEach(button => {

    button.addEventListener("click", () => {

        document.querySelector(".active").classList.remove("active");
        button.classList.add("active");

        const filter = button.dataset.name;

        images.forEach(image => {

            if(filter === "all" || image.dataset.name === filter){
                image.style.display = "block";
            } else {
                image.style.display = "none";
            }

        });

    });

});

const galleryImages = document.querySelectorAll(".gallery img");
const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const closeBtn = document.querySelector(".close");

galleryImages.forEach(img => {

    img.addEventListener("click", () => {

        lightbox.style.display = "flex";
        lightboxImg.src = img.src;

    });

});

closeBtn.addEventListener("click", () => {
    lightbox.style.display = "none";
});

lightbox.addEventListener("click", (e) => {

    if(e.target !== lightboxImg){
        lightbox.style.display = "none";
    }

});