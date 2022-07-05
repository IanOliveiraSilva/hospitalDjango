const eventos = document.querySelectorAll(".event");
const titles = document.querySelectorAll(".event-title");
const infos = document.querySelectorAll(".event-info");

let toggleEvent = [];

for (let i = 0; i < titles.length; i++) {
    toggleEvent.push("off");
}

for (let i = 0; i < eventos.length; i++) {
  eventos[i].addEventListener("click", function () {
    if (toggleEvent[i] == "off") {
      titles[i].style.color = "var(--darkGreen)";
      infos[i].style.whiteSpace = "pre-line";
      console.log(infos[i].innerHTML);
      console.log(i);
      toggleEvent[i] = "on";
    } else {
        titles[i].style.color = "black";
        infos[i].style.whiteSpace = "nowrap";
        toggleEvent[i] = "off";
    }
  });
}
