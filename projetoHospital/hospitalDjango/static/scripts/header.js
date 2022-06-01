const $logo = document.querySelector(".header__title--logo");
const $hospitalName = document.querySelector(".header__title--title");
const $menu = document.querySelector(".header__menu");
const $lines = document.querySelector(".header__menu--menu");
const $linesImage = document.querySelector(".header__menu--menu-image");
const $menuAlt = document.querySelector(".header__menu--title");
const $menuOptions = document.querySelector(".menu-options");

window.onscroll = function () {
  scrollFunction();
};

function sendTo(web) {
  window.location.href = web;
}

function scrollFunction() {
  if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
    const fontSizeTitle = 40 / 16;
    const fontSizeAlt = 15 / 16;

    $logo.style.width = "40px";

    $hospitalName.style.fontSize = `${fontSizeTitle}rem`;

    $menuAlt.style.fontSize = `${fontSizeAlt}rem`;
    $menuAlt.style.margin = "40px 0 0 0";

    $menuOptions.style.margin = "-8% 0 0 9.5%";
    $menuOptions.style.padding = "5% 0 0 0";

    $linesImage.style.width = "40px";
  } else {
    const fontSizeTitle = 56 / 16;
    const fontSizeAlt = 20 / 16;

    $logo.style.width = "80px";

    $hospitalName.style.fontSize = `${fontSizeTitle}rem`;

    $menuAlt.style.fontSize = `${fontSizeAlt}rem`;
    $menuAlt.style.margin = "50px 0 0 0";

    $menuOptions.style.margin = "-1% 0 0 9.5%";
    $menuOptions.style.padding = "0 0 0 0";

    $linesImage.style.width = "50px";
  }
}

$menu.addEventListener("mouseover", function () {
  $menuOptions.style.display = "block";
});

$menuOptions.addEventListener("mouseover", function () {
  $menuOptions.style.display = "block";
});

$menuOptions.addEventListener("mouseout", function () {
  $menuOptions.style.display = "none";
});
