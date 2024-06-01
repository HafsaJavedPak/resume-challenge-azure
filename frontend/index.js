function fetchVisitorCount() {
  const url = "https://my-best-portfolio-function.azurewebsites.net/api/count"; 
  let regex = /\d+/;
  let match;
  fetch(url)
    .then(response => response.text()) // Visitor Count incremented to [num].
    .then(text => {
    // to extract number from response
      match = text.match(regex);
      if (match) {
          const visitorCount = parseInt(match[0]);
          const visitorCountElement = document.getElementById("visitor-count");
          visitorCountElement.textContent = `${visitorCount} vistor${visitorCount == 1 ? "":"s"}`;
      } 
      else {
          console.log(text); // Output: "Visitor count incremented to 25."
      }
    })
    .catch(error => console.error(error));
}

window.onload =  () => {
  fetchVisitorCount();
}
