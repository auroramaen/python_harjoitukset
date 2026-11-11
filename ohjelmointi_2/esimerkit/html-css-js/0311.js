/*tuodaan kuva*/
const logo =
  "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500";

/*asetetaan luokka logo kuvaksi*/
document.querySelector("#logo").innerHTML = `<img src="${logo}" alt="Logo">`;

/*asetetaan myös bodyyn logokuva*/
document.querySelector("body").innerHTML += `<img src="${logo}" alt="Logo">`;

const p = document.createElement("p");
p.innerHTML = "Minun hieno paragraph";

document.body.appendChild(p);
document.querySelector("body").appendChild(p);

/*aina kun eventtiin tulee click, tätä funktiota kutsutaan*/
document.querySelector("button").addEventListener("click", () => {
  document.querySelector("body").innerHTML = "";
  /*alert("VAROITUS");*/
});

document.querySelector(".delete-cat").addEventListener("click", () => {
  document.querySelector("#logo").innerHTML = "";
});
