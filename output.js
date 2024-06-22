window.onload = function () {
  var navMenu = document.getElementById("nav-menu");
  var navItems = navMenu.getElementsByTagName("li");
  for (var i = 0; i < navItems.length; i++) {
    navItems[i].addEventListener("mouseenter", function (event) {
      var subMenu = this.getElementsByTagName("ul")[0];
      if (subMenu) {
        subMenu.style.display = "block";
      }
    });
    navItems[i].addEventListener("mouseleave", function (event) {
      var subMenu = this.getElementsByTagName("ul")[0];
      if (subMenu) {
        subMenu.style.display = "none";
      }
    });
  }
};
