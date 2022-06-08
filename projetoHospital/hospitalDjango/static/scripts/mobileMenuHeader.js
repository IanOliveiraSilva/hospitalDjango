/* @media small devices*/
const $menuOptions = document.querySelector(".menu-options");
const $menuDevices = document.querySelector(".header__menu--devices");
const $menuDevOpt = document.querySelector(".menu-device-options");


$menuDevOpt.addEventListener("mouseover", function () {
  $menuDevOpt.style.display = "block";
});

$menuDevices.addEventListener("mouseover", function () {
    $menuOptions.style.display = "block";
});
  
$menuDevOpt.addEventListener("mouseover", function () {
  $menuDevOpt.style.display = "none";
});