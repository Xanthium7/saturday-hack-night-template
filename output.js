javascript;
window.addEventListener("DOMContentLoaded", (event) => {
  // Sticky Navigation Bar
  var navbar = document.getElementById("navbar");
  var sticky = navbar.offsetTop;
  function stickyNav() {
    if (window.pageYOffset >= sticky) {
      navbar.classList.add("sticky");
    } else {
      navbar.classList.remove("sticky");
    }
  }
  window.onscroll = function () {
    stickyNav();
  };

  // Animations on Hover
  var foodItems = document.getElementsByClassName("food-item");
  for (let i = 0; i < foodItems.length; i++) {
    foodItems[i].addEventListener("mouseover", function () {
      foodItems[i].style.transform = "scale(1.1)";
    });
    foodItems[i].addEventListener("mouseout", function () {
      foodItems[i].style.transform = "scale(1)";
    });
  }

  // Dynamic Content Loading
  var sections = ["starters", "main", "desserts"];
  sections.forEach((section) => {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById(section).innerHTML = this.responseText;
      }
    };
    xmlhttp.open("GET", section + ".txt", true);
    xmlhttp.send();
  });
});
