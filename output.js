document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });
});

let projectElements = document.querySelectorAll(".project");

projectElements.forEach((project) => {
  project.addEventListener("mouseover", function () {
    this.querySelector(".project-description").style.visibility = "visible";
  });

  project.addEventListener("mouseout", function () {
    this.querySelector(".project-description").style.visibility = "hidden";
  });
});
