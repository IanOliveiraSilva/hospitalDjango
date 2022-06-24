const phone = document.querySelector("#contato-telefone");
const email = document.querySelector("#contato-email");
const copied = document.querySelectorAll(".copied");

var index = 0;

function copiedBubble(index){
    copied[index].style.display = "flex";
    !index ? copied[index].style.left = "50px" : copied[index].style.right = "85px";
    setTimeout(() => {
        copied[index].style.display = "none";

    }, 1000);
}

phone.onclick = function () {
  document.execCommand("copy");
  copiedBubble(0);
};

phone.addEventListener("copy", function (event) {
    event.preventDefault();
    if (event.clipboardData) {
        event.clipboardData.setData("text/plain", phone.textContent);
    }
});

email.onclick = function () {
    document.execCommand("copy");
    copiedBubble(1);
};

email.addEventListener("copy", function (event) {
  event.preventDefault();
  if (event.clipboardData) {
    event.clipboardData.setData("text/plain", email.textContent);
  }
});
