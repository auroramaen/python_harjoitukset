"use strict";
const vuosilukuStr = prompt("Anna vuosiluku");
const vuosiluku = parseInt(vuosilukuStr);

if ((vuosiluku % 4 === 0 && vuosiluku % 100 !== 0) || (vuosiluku % 400 === 0)) {
    document.querySelector("#tulos").innerHTML = 
    `Vuosi ${vuosiluku} on karkausvuosi.`;
} 
else {
    document.querySelector("#tulos").innerHTML = 
    `Vuosi ${vuosiluku} ei ole karkausvuosi.`;
}