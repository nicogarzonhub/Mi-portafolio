function mostrarSeccion(id) {
  document.querySelectorAll(".proyectos").forEach(sec => {
    sec.classList.remove("activo");
  });

  document.getElementById(id).classList.add("activo");
}

function mostrarSemana(area, semana) {
  document
    .querySelectorAll(`.${area}-semana`)
    .forEach(div => div.classList.remove("activo"));

  document
    .querySelector(`.${area}-semana[data-semana="${semana}"]`)
    .classList.add("activo");
}
