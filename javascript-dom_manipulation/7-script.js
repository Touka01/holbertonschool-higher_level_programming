const apiUrl = "https://swapi-api.hbtn.io/api/films/?format=json"; // Define the API URL
const listMoviesElement = document.getElementById("list_movies"); // Select the element with the id 'list_movies'

async function fetchAndListMovies() { // Define the function
  try {
    const response = await fetch(apiUrl);  // Fetch the data
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`); // Check if the response is ok
    const data = await response.json(); // Parse the data

    data.results.forEach((movie) => { // Loop through the data
      const listItem = document.createElement("li"); // Create a new list item
      listItem.textContent = movie.title; // Add the title to the list item
      listMoviesElement.appendChild(listItem); // Add the list item to the list
    });
  } catch (error) { // Handle the error
    console.error("Fetch error:", error); // Log the error
  }
}

fetchAndListMovies(); // Call the function