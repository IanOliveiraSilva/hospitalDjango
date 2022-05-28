const $banners = document.querySelectorAll(".banner");
const $sideMenu = document.querySelectorAll(".side-menu_arrow");
const $buttonDonation = document.querySelector(".donation-button");
const $moveButtons = document.querySelector(".move-buttons");
const $dot = document.querySelectorAll(".dot");
const $back = document.querySelector(".back");
const $forward = document.querySelector(".forward");

$moveButtons.addEventListener("mouseover", function () {
  $back.style.fontSize = "50px";
  $forward.style.fontSize = "50px";
});

$moveButtons.addEventListener("mouseout", function () {
  $back.style.fontSize = "15px";
  $forward.style.fontSize = "15px";
});

var slidePosition = 1;
slideShowManual(slidePosition);

// forward/Back controls
function plusSlides(n) {
  slideShowManual((slidePosition += n));
}

//  images controls
function currentSlide(n) {
  slideShowManual((slidePosition = n));
}

function slideShowManual(n) {
  let i;
  if (n > $banners.length) {
    slidePosition = 1;
  }
  if (n < 1) {
    slidePosition = $banners.length;
  }
  for (i = 0; i < $banners.length; i++) {
    $banners[i].style.display = "none";
  }
  for (i = 0; i < $dot.length; i++) {
    $dot[i].className = $dot[i].className.replace(" enable", "");
  }
  $banners[slidePosition - 1].style.display = "block";
  $dot[slidePosition - 1].className += " enable";
}

var slidePosition = 0;
slideShowAutomatic();

function slideShowAutomatic() {
  var i;
  for (i = 0; i < $banners.length; i++) {
    $banners[i].style.display = "none";
  }
  for (i = 0; i < $dot.length; i++) {
    $dot[i].className = $dot[i].className.replace(" enable", "");
  }
  slidePosition++;
  if (slidePosition > $banners.length) {
    slidePosition = 1;
  }
  $banners[slidePosition - 1].style.display = "block";
  $dot[slidePosition - 1].className += " enable";
  setTimeout(slideShowAutomatic, 12000);
}

$buttonDonation.addEventListener("click", function () {
  location.href = "doacao";
});

function selectMenu() {
  for (let index = 0; index < $sideMenu.length; index++) {
    $sideMenu[index].addEventListener("click", function () {
      if (index == 0) {
        location.href = "doacao";
      }
      if (index == 1) {
        location.href = "guia-medico";
      }
      if (index == 2) {
        location.href = "eventos";
      }
      if (index == 3) {
        location.href = "convenio";
      }
      if (index == 4) {
        location.href = "transparencia";
      }
    });
  }
}

selectMenu();
