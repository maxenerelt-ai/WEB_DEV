const wrapper = document.getElementById("chickenjoe");
const img = document.getElementById("imagesecret");

wrapper.addEventListener("mouseenter", () => {
    img.style.opacity = "1";
});

wrapper.addEventListener("mouseleave", () => {
    img.style.opacity = "0";
});
