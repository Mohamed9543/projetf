document.addEventListener("DOMContentLoaded", function() {
    const editButton = document.querySelector(".edit-btn");
    const SettingButton = document.querySelector(".Setting-btn");
    const SettingMenu = document.getElementById("Setting-bar");
    
    // Toggle settings sidebar
    SettingButton.addEventListener("click", function() {
        SettingMenu.classList.toggle("show");
    });
    
    // Edit username functionality
    editButton.addEventListener("click", function() {
        let username = prompt("Enter new username:", "username");
        if (username) {
            document.querySelector("h2").textContent = username;
        }
    });
});