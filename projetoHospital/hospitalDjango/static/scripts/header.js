const $logo = document.querySelector(".header__title--logo ");
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


/*============================ M O B I L E      D E V I C E ============================*/



const $logoSD = document.querySelector(".header__title--logo-small-device");
const $hospitalNameSD = document.querySelector(".header__title--title-small-device");
const $menuSD = document.querySelector(".header__menu-small-device");
const $linesSD = document.querySelector(".header__menu--menu-small-device");
const $linesImageSD = document.querySelector(".header__menu--menu-image-small-device");
const $menuAltSD = document.querySelector(".header__menu--title-small-device");
const $menuOptionsSD = document.querySelector(".menu-options-small-device");




window.onscroll = function () {
  scrollFunction();
};

function sendTo(web) {
  window.location.href = web;
}

function scrollFunction() {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
    const fontSizeTitleSD = 13.3 / 5.3;
    const fontSizeAltSD = 5 / 5.3;

    $logoSD.style.width = "13.3px";

    $hospitalNameSD.style.fontSize = `${fontSizeTitleSD}rem`;

    $menuAltSD.style.fontSize = `${fontSizeAltSD}rem`;
    $menuAltSD.style.margin = "13.3px 0 0 0";

    $menuOptionsSD.style.margin = "-2.6% 0 0 3.16%";
    $menuOptionsSD.style.padding = "1.6% 0 0 0";

    $linesImageSD.style.width = "13.3px";
  } else {
    const fontSizeTitleSD = 18.6 / 5.3;
    const fontSizeAltSD = 6.6 / 5.3;

    $logoSD.style.width = "26.6px";

    $hospitalNameSD.style.fontSize = `${fontSizeTitleSD}rem`;

    $menuAltSD.style.fontSize = `${fontSizeAltSD}rem`;
    $menuAltSD.style.margin = "16.6px 0 0 0";

    $menuOptionsSD.style.margin = "-0.33% 0 0 3.16%";
    $menuOptionsSD.style.padding = "0 0 0 0";

    $linesImageSD.style.width = "16.6px";
  }
}