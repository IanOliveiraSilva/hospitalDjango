const $sideMenu = document.querySelectorAll(".side-menu_arrow");
const $buttonDonation = document.querySelector(".donation-button");

$buttonDonation.addEventListener("click", function () {
  location.href = "doacao";
});

function addBoardListeners() {
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

addBoardListeners();
