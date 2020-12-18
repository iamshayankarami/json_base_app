<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3pro.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-teal.css">
<body style="max-width:600px">

<nav class="w3-sidebar w3-bar-block w3-card" id="mySidebar">
<div class="w3-container w3-theme-d2">
  <span onclick="closeSidebar()" class="w3-button w3-display-topright w3-large">X</span>
  <br>
</div>
<a class="w3-bar-item w3-button" href="#">Movies</a>
<a class="w3-bar-item w3-button" href="#">Friends</a>
<a class="w3-bar-item w3-button" href="#">Messages</a>
</nav>

<header class="w3-bar w3-card w3-theme">
  <button class="w3-bar-item w3-button w3-xxxlarge w3-hover-theme" onclick="openSidebar()">&#9776;</button>
  <h1 class="w3-bar-item">Movies</h1>
</header>

<div class="w3-container">
<hr>
<div class="w3-cell-row">
  <div class="w3-cell w3-container">
    <h3>Frozen</h3>
    <p>The response to the animations was ridiculous.</p>
  </div>
</div>  
<hr>
<div class="w3-cell-row">
  <div class="w3-cell w3-container">
    <h3>The Fault in Our Stars</h3>
    <p>Touching, gripping and genuinely well made.</p>
  </div>
</div>
<hr>
</div>


<script>
closeSidebar();
function openSidebar() {
  document.getElementById("mySidebar").style.display = "block";
}

function closeSidebar() {
  document.getElementById("mySidebar").style.display = "none";
}
</script>

</body>