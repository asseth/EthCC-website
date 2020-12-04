function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

function vcReadMore() {
  var extra = document.getElementById("extra");
  var moreText = document.getElementById("plus");
  var vcbtnText = document.getElementById("vcBtn");

  if (extra.style.display === "none") {
    extra.style.display = "inline";
    vcbtnText.innerHTML = "Read More";
    plus.style.display = "none";
  } else {
    extra.style.display = "none";
    vcbtnText.innerHTML = "Read Less";
    plus.style.display = "inline";
  }
}


var n = 30; // Nombre final du compteur
var cpt = 0; // Initialisation du compteur
var m = 64;
var o = 36;
var duree = 2; // Durée en seconde pendant laquel le compteur ira de 0 à 15
var delta = Math.ceil((duree * 1000) / n); // On calcule l'intervalle de temps entre chaque rafraîchissement du compteur (durée mise en milliseconde)
var node =  document.getElementById("compteur"); // On récupère notre noeud où sera rafraîchi la valeur du compteur
var equity = document.getElementById("equity");
var token = document.getElementById("token");


// function countdownStartups() {
//   node.innerHTML = cpt;
//   if( cpt < n ) {
//      setTimeout(countdownStartups, delta);

//   }
// }
// function countdownEquity() {
//   equity.innerHTML = ++cpt;
//   if( cpt < m) {
//      setTimeout(countdownEquity, delta)
//   }
// }
// function countdownToken() {
//   token.innerHTML = cpt;
//   if( cpt < o) {
//      setTimeout(countdownToken, delta)
//   }
// }

// setTimeout(function() {
//   countdownStartups() // runs first
//   countdownEquity() // runs second
//   countdownToken()
// }, delta)

