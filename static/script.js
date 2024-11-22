// Function to open the popup with title and description
function openPopup(title, description) {
    document.getElementById("popup-title").textContent = title;
    document.getElementById("popup-description").textContent = description;
    document.getElementById("popup-description").classList.add("hidden");
    document.getElementById("popup").style.display = "flex";
}

// Function to close the popup
function closePopup() {
    document.getElementById("popup").style.display = "none";
}

// Function to reveal content in the popup
function revealContent() {
    document.getElementById("popup-description").classList.toggle("hidden");
}