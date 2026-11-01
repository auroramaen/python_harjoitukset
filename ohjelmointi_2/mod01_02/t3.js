"use strict";
const luku1Str = prompt("Anna kokonaisluku:");
const luku1 = parseInt(luku1Str);

const luku2Str = prompt("Anna toinen kokonaisluku:");
const luku2 = parseInt(luku2Str);

const luku3Str = prompt("Anna kolmas kokonaisluku:");
const luku3 = parseInt(luku3Str);

const summa = luku1 + luku2 + luku3;
const tulo = luku1 * luku2 * luku3;
const keskiarvo = summa / 3;

document.querySelector("#target").innerHTML = 
  `Lukujen ${luku1}, ${luku2} ja ${luku3} summa on ${summa}, tulo on ${tulo} ja keskiarvo on ${keskiarvo}`;