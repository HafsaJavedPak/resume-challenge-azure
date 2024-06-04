// function fetchVisitorCount() {
//     const url = "https://your-azure-function-endpoint.com/api/getVisitorCount"; // Replace with your actual function URL
  
//     fetch(url)
//       .then(response => response.json())  // Parse the JSON response
//       .then(data => {
//         const visitorCountElement = document.getElementById("visitorCount");
//         visitorCountElement.textContent = data.count;  // Update the element content
//       })
//       .catch(error => console.error(error));  // Handle errors
//   }


let visitorCount;

window.onload =  () => {
    let num = localStorage.getItem("visitors");
    let res;
    if (num == null) {
        num = 1;
        localStorage.setItem("visitors", num);
    }
    else {
        num++;
        localStorage.setItem("visitors",num);
    }
    const visitorCountElement = document.getElementById("visitor-count");
    visitorCountElement.textContent = `${num} vistor${num == 1 ? "":"s"}`;

}
  