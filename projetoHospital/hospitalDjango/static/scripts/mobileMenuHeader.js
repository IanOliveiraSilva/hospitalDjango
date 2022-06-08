/* @media small devices*/
const $menuOptions = document.querySelector(".menu-options");
const $menuDevices = document.querySelector(".header__menu--devices");
const $deviceMenu = document.querySelector(".device-menu");


$deviceMenu.addEventListener("mouseover", function () {
    $deviceMenu.style.display = "block";
  });
  
  $deviceMenu.addEventListener("mouseover", function () {
    $deviceMenu.style.display = "none";
  });