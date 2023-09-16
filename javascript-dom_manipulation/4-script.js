document.getElementById('add_item').addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    // Create a new <li> element and add it to the <ul> element

    const myList = document.querySelector('.my_list');
    myList.appendChild(newItem);
}); // Select the <ul> element with class 'my_list' and append a new <li> element