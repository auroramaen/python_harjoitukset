function addCode() {
  const uusiLista = document.getElementById("target");

  const li1 = document.createElement("li");
  li1.textContent = "First item";
  uusiLista.appendChild(li1);

  const li2 = document.createElement("li");
  li2.textContent = "Second item";
  li2.classList.add("my-item");
  uusiLista.appendChild(li2);

  const li3 = document.createElement("li");
  li3.textContent = "Third item";
  uusiLista.appendChild(li3);
}
