/* @media small devices*/
const $menuOptions = document.querySelector(".menu-options");
const $menuDevices = document.querySelector(".header__menu--devices");



$menuOptions.addEventListener("mouseover", function () {
  $menuOptions.style.display = "block";
});

$menuDevices.addEventListener("mouseover", function () {
    $menuOptions.style.display = "block";
});
  
$menuOptions.addEventListener("mouseover", function () {
  $menuOptions.style.display = "none";
});