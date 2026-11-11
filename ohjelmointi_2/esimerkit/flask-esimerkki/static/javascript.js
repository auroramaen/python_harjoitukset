const haeLottorivi = async () => {
  // datan haku rajapinnasta
  const response = await fetch("/viikon-lottorivi");

  console.log("response", response);

  //datan muutos json muotoon
  const data = await response.json();

  console.log("data", data);
  console.log("Ensimmäinen rivi", data[0]);
};
