function getRandomInt(max) {
      return Math.floor(Math.random() * max);
}

"use strict";
const nimi = prompt("Anna nimesi:");

const luku = getRandomInt(4);
if (luku == 1) {
    document.querySelector("#target").innerHTML = 
    `${nimi}, sinä olet Korpinkynsi.`;
} 
else if (luku == 2) {
    document.querySelector("#target").innerHTML = 
    `${nimi}, sinä olet Puuskupuh.`;
}
else if (luku == 3) {
    document.querySelector("#target").innerHTML = 
    `${nimi}, sinä olet Rohkelikko.`;
}
else {
    document.querySelector("#target").innerHTML = 
    `${nimi}, sinä olet Luihunen.`;
}


