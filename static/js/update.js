function fetchData() {
    fetch('/update_data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('data-div').innerHTML = data.html;
        });
}

// Poll every 2 seconds
setInterval(fetchData, 2000);

// Fetch immediately on page load
fetchData();
