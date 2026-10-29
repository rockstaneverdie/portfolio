// Click-to-zoom for case images.
const box = document.querySelector(".lightbox");
const big = box.querySelector("img");

document.addEventListener("click", (ev) => {
  const img = ev.target.closest(".media img[data-zoom]");
  if (img) {
    big.src = img.currentSrc || img.src;
    big.alt = img.alt;
    box.hidden = false;
    box.querySelector("button").focus();
  } else if (!box.hidden && ev.target.closest(".lightbox")) {
    box.hidden = true;
  }
});
document.addEventListener("keydown", (ev) => {
  if (ev.key === "Escape") box.hidden = true;
});
