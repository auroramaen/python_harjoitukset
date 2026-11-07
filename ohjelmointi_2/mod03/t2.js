"use strict";

const lkmStr = prompt("Anna osallistujien lukumäärä");
const lkm = parseInt(lkmStr);

const osallistujat = [];

for (let i = 0; i < lkm; i++) {
  const nimi = prompt(`Anna osallistujan ${i + 1} nimi:`);
  osallistujat.push(nimi);
}

osallistujat.sort((a, b) => a.localeCompare(b));

osallistujat.forEach(function (item) {
  var li = document.createElement("li");
  var text = document.createTextNode(item);
  li.appendChild(text);
  document.getElementById("htmlList").appendChild(li);
});
