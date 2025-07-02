const input = document.getElementById('inputTexto');
const parrafo = document.getElementById('parrafo');

input.addEventListener('input', () => {
  parrafo.innerText = input.value;
});
