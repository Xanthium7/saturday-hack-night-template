Here's a simple JavaScript code which will animate the scroll to respective sections when navbar links are clicked:

```javascript
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

let projectElements = document.querySelectorAll('.project');

projectElements.forEach(project => {
    project.addEventListener('mouseover', function() {
        this.querySelector('.project-description').style.visibility = 'visible';
    });

    project.addEventListener('mouseout', function() {
        this.querySelector('.project-description').style.visibility = 'hidden';
    });
});
```

This code includes smooth scrolling for links and showing project descriptions on hover.