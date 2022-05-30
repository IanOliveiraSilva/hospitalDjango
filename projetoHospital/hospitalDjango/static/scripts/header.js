const $logo = document.querySelector(".header__title--logo");
const $hospitalName = document.querySelector(".header__title--title");
const $menu = document.querySelector(".header__menu");
const $lines = document.querySelector(".header__menu--menu");
const $linesImage = document.querySelector(".header__menu--menu-image");
const $closeImage = document.querySelector(".header__menu--close-image");
const $close = document.querySelector(".header__menu--close");
const $menuAlt = document.querySelector(".header__menu--title");
const $menuOptions = document.querySelector(".menu-options");

window.onscroll = function () {
  scrollFunction();
};

function homeLink(web) {
  window.location.href = web;
}

function pacienteLink(web) {
  window.location.href = web;
}

function historiaHospitalLink(web) {
  window.location.href = web;
}

function diretoriaHospitalLink(web) {
  window.location.href = web;
}

function historiaFundacaoLink(web) {
  window.location.href = web;
}

function diretoriaFundacaoLink(web) {
  window.location.href = web;
}

function nossaMissaoLink(web) {
  window.location.href = web;
}

function resultadosLink(web) {
  window.location.href = web;
}

function consultasLink(web) {
  window.location.href = web;
}

function telemedicinaLink(web) {
  window.location.href = web;
}

function parceirosLink(web) {
  window.location.href = web;
}

function eventosLink(web) {
  window.location.href = web;
}

function noticiasLink(web) {
  window.location.href = web;
}

function trabalheLink(web) {
  window.location.href = web;
}

function ouvidoriaLink(web) {
  window.location.href = web;
}

function pesquisaLink(web) {
  window.location.href = web;
}

function residenteLink(web) {
  window.location.href = web;
}


function scrollFunction() {
  if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
    const fontSizeTitle = 40 / 16;
    const fontSizeAlt = 15 / 16;

    $logo.style.width = "40px";

    $hospitalName.style.fontSize = `${fontSizeTitle}rem`;

    $closeImage.style.width = "30px";
    $menuAlt.style.fontSize = `${fontSizeAlt}rem`;
    $menuAlt.style.margin = "40px 0 0 0";

    $menuOptions.style.margin = "-1% 0 0 9.5%";

    $linesImage.style.width = "40px";
  } else {
    const fontSizeTitle = 56 / 16;
    const fontSizeAlt = 20 / 16;

    $logo.style.width = "80px";

    $hospitalName.style.fontSize = `${fontSizeTitle}rem`;

    $closeImage.style.width = "40px";
    $menuAlt.style.fontSize = `${fontSizeAlt}rem`;
    $menuAlt.style.margin = "50px 0 0 0";

    $menuOptions.style.margin = "0 0 0 9.5%";

    $linesImage.style.width = "50px";
  }
}

$menu.addEventListener("mouseover", function () {
  $lines.style.display = "none";
  $close.style.display = "block";
  $menuAlt.innerHTML = "Fechar";
  $menuOptions.style.display = "block";
});

$menuOptions.addEventListener("mouseover", function () {
  $lines.style.display = "none";
  $close.style.display = "block";
  $menuAlt.innerHTML = "Fechar";
  $menuOptions.style.display = "block";
});

$menuOptions.addEventListener("mouseout", function () {
  $lines.style.display = "block";
  $close.style.display = "none";
  $menuAlt.innerHTML = "Menu";
  $menuOptions.style.display = "none";
});
