const boton = document.getElementById('boton');
const titulo = document.getElementById('titulo');

boton.addEventListener('click', () => {
  titulo.innerText = '¡Has cambiado el texto con JavaScript!';
});
