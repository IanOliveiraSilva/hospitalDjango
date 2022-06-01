const $wrapper = document.querySelectorAll(".donate-wrapper");
const $images = document.querySelectorAll(".donate-image");
const $infos = document.querySelectorAll(".donate-info-wrapper");

function openInfos() {
  for (let index = 0; index < $wrapper.length; index++) {
    $images[index].addEventListener("mouseover", function () {
      $infos[index].style.display = "block";
      $infos[index].style.display = "flex";
      $images[index].style.display = "none";
    });
    $infos[index].addEventListener("mouseout", function () {
      $infos[index].style.display = "none";
      $images[index].style.display = "block";
    });
  }
}

openInfos();
