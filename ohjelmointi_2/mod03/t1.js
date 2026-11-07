"use strict";
const numerot = [];

const num1 = prompt("Anna ensimmäinen luku");
const num2 = prompt("Anna toinen luku");
const num3 = prompt("Anna kolmas luku");
const num4 = prompt("Anna neljäs luku");
const num5 = prompt("Anna viides luku");

numerot.push(num1, num2, num3, num4, num5);

for (let i = numerot.length - 1; i >= 0; i--) {
  console.log(`${numerot[i]}`);
}
