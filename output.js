Here is the JavaScript code to add the requested functionality:

```javascript
// Initialize all sections
const sections = document.querySelectorAll('section');

// Add an event listener for the 'click' event on each section
sections.forEach(section => {
  section.addEventListener('click', event => {
    // Check if the clicked element is a button
    if (event.target.nodeName === 'BUTTON') {
      // Execute your order function here
      orderFood(event.target.parentNode);
    }
  });
});

// Add a hover effect to each food listing
const foodListings = document.querySelectorAll('.food-listing');

foodListings.forEach(listing => {
  listing.addEventListener('mouseover', event => {
    event.target.style.transform = 'scale(1.05)';
    event.target.style.transition = 'transform 0.3s';
  });

  listing.addEventListener('mouseout', event => {
    event.target.style.transform = 'none';
  });
});

// Function to smoothly scroll to a section when its corresponding nav link is clicked
document.querySelector('#navbar').addEventListener('click', function (event) {
  event.preventDefault();
  if (event.target.nodeName === 'A') {
    document.querySelector(event.target.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  }
});

// Function to process food order
function orderFood(foodListing) {
  // Extract the food description from the listing
  const foodDescription = foodListing.querySelector('.food-description').innerText;

  // Place order...
  console.log(`Order received for ${foodDescription}`);
}
```
Please note that this JavaScript code assumes that there is a function to process the food order when the "Order Now" button is clicked. It uses `console.log` to simulate this function, but you'll need to replace this with actual code to process the order.