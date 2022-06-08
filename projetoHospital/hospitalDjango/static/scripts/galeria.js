var modal = document.querySelector(".modal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var images = document.querySelectorAll(".galery-image");
var modalImg = document.querySelector(".modal-image");
var modalTitle = document.querySelector(".modal-title");

for (let i = 0; i < images.length; i++) {
  images[i].onclick = function () {
    console.log(i);
    modal.style.display = "block";
    modalImg.src = this.src;
    modalTitle.innerHTML = this.alt;
  };
}

// Get the <span> element that closes the modal
var span = document.querySelectorAll(".close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

var prev = document.querySelectorAll(".modal-previous");
var next = document.querySelectorAll(".modal-next");

let imgs = [];
let alts = [];
for (let index = 0; index < images.length; index++) {
  imgs.push(images[index].src);
  alts.push(images[index].getAttribute("alt"));
}

console.log(imgs);

for (let i = 0; i < prev.length; i++) {
  let auxImg;
  let auxAlt;
  prev[i].addEventListener("click", function () {
    if (i === 0) {
      auxImg = imgs[0];
      auxAlt = alts[0];
      imgs.shift();
      alts.shift();
      imgs.push(auxImg);
      alts.push(auxAlt);

      for (let j = 0; j < imgs.length; j++) {
        modalImg.src = imgs[j];
        modalImg.alt = alts[j];
      }
    }
  });
}

for (let i = 0; i < next.length; i++) {
  let auxImg;
  let auxAlt;
  next[i].addEventListener("click", function () {
    if (i === 0) {
      auxImg = imgs[imgs.length - 1];
      auxAlt = alts[alts.length - 1];
      imgs.pop();
      alts.pop();
      imgs.unshift(auxImg);
      alts.unshift(auxAlt);

      for (let j = 0; j < imgs.length; j++) {
        modalImg.src = imgs[j];
        modalImg.alt = alts[j];
      }
    }
  });
}
