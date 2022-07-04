const medico = document.querySelector("#funcao-medico");
const area = document.querySelector("#form-area");
const enfermeiro = document.querySelector("#funcao-enfermeiro");
const atendente = document.querySelector("#funcao-atendente");
const voluntario = document.querySelector("#funcao-voluntario");
const outros = document.querySelector("#funcao-outros");
const funcao = document.querySelector("#funcao-informe");

medico.addEventListener("click", function () {
  if (medico.checked) {
    funcao.disabled = true;
    area.disabled = false;
  }
});

enfermeiro.addEventListener("click", function () {
  if (enfermeiro.checked) {
    funcao.disabled = true;
    area.disabled = true;
  }
});

atendente.addEventListener("click", function () {
  if (atendente.checked) {
    funcao.disabled = true;
    area.disabled = true;
  }
});

voluntario.addEventListener("click", function () {
  if (voluntario.checked) {
    funcao.disabled = true;
    area.disabled = true;
  }
});

outros.addEventListener("click", function () {
  if (outros.checked) {
    funcao.disabled = false;
    area.disabled = true;
  }
});