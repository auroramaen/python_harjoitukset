"use strict";

function addCode() {
  const names = ["John", "Paul", "Jones"];
  const kohde = document.getElementById("target");

  for (let i = 0; i < names.length; i++) {
    kohde.innerHTML += `<li>${names[i]}</li>`;
  }
}
