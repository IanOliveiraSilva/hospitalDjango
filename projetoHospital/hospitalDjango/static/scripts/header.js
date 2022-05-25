const $logo = document.querySelector(".header__title--logo");
const $hospitalName = document.querySelector(".header__title--title");
const $menu = document.querySelector(".header__menu");
const $lines = document.querySelectorAll(".header__menu--line");
const $menuAlt = document.querySelector(".header__menu--title");
const $departments = document.querySelector(".menu--departments");

window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
    const fontSizeTitle = 40 / 16;
    const fontSizeAlt = 15 / 16;

    $logo.style.width = "40px";

    $hospitalName.style.fontSize = `${fontSizeTitle}rem`;

    $menuAlt.style.fontSize = `${fontSizeAlt}rem`;

    $menu.style.width = "40px";
    $menu.style.margin = "0";
    $departments.style.padding = "4% 0 0 0";

    for (let $i = 0; $i < $lines.length; $i++) {
      $lines[$i].style.height = "2px";
    }
  } else {
    const fontSizeTitle = 56 / 16;
    const fontSizeAlt = 20 / 16;

    $logo.style.width = "70px";

    $hospitalName.style.fontSize = `${fontSizeTitle}rem`;

    $menuAlt.style.fontSize = `${fontSizeAlt}rem`;

    $menu.style.width = "50px";
    $menu.style.margin = "2vh 0 0 0";
    $departments.style.padding = "6% 0 0 0";

    for (let $i = 0; $i < $lines.length; $i++) {
      $lines[$i].style.height = "4px";
    }
  }
}

$menu.addEventListener("click", function () {
  console.log("a");
  if ($departments.style.display === "none") {
    $departments.style.display = "block";
  } else {
    $departments.style.display = "none";
  }
});
