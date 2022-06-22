const $images = document.querySelectorAll(".donate-image");
let $modal = document.querySelectorAll(".modal");
let $closeBtnDontation = document.querySelectorAll(".close");

function displayInfos() {
  for (let i = 0; i < $images.length; i++) {
    $images[i].onclick = function () {
      $modal[i].style.display = "flex";
      close(i);
    };
  }
}

function close(i) {
  $closeBtnDontation[i].onclick = function () {
    $modal[i].style.display = "none";
  };
}

displayInfos();
