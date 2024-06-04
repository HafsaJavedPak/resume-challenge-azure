function getCookie(name) {
  let match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? match[2] : null;
}

function setCookie(name, value, days) {
  let expires = "";
  if (days) {
      let date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = "; expires=" + date.toUTCString();
  }
  document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function trackVisitor() {
  let visited = getCookie('visitedBefore');
  let url;
  if (!visited) {
      setCookie('visitedBefore', 'true', 365); // Set cookie for 1 year
      url = "https://my-best-portfolio-function.azurewebsites.net/api/count/new"; 
  } 
  else {
    url = "https://my-best-portfolio-function.azurewebsites.net/api/count"; 
  }
  // calls azure function
  let regex = /\d+/;
  let match;
  fetch(url)
    .then(response => response.text()) // Visitor Count is [num].
    .then(text => {
    // to extract number from response
      match = text.match(regex);
      if (match) {
          const visitorCount = parseInt(match[0]);
          const visitorCountElement = document.getElementById("visitor-count");
          visitorCountElement.textContent = `${visitorCount} vistor${visitorCount == 1 ? "":"s"}`;
      } 
      else {
          console.log(text); // Output: "Visitor count is 25."
      }
    })
    .catch(error => console.error(error));
    
    // updates visitor number
    const visitorCountElement = document.getElementById("visitor-count");
    visitorCountElement.textContent = `${num} vistor${num == 1 ? "":"s"}`;
}

document.addEventListener('DOMContentLoaded', (event) => {
  trackVisitor();
});
