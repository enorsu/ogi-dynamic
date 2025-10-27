

const dropdown = document.getElementById("dropdown");
const windows = document.getElementsByClassName("window");
const closebuttons = document.getElementsByClassName("close");


dropdown.addEventListener("click", displayWindow);

// god bypass
function displayWindow() {
    // before making clear windows
    clearWindows();
    let window = windows.item(dropdown.value);
    // default display style
    window.style.display = "";
}
// HOW TO READ FOR RETARDS 2025
function clearWindows() {
    for (let i = 0; i < windows.length; i++) {
        let window = windows.item(i);
        window.style.display = "none";
    }
}

setupWindows();
function setupWindows() {

    // for close buttons to work
    // (it just removes all windows XD)
    for (let i = 0; i < closebuttons.length; i++) {
        let item = closebuttons.item(i);

        item.addEventListener("click", clearWindows);
    }
    
    // this one hides all of them and does some bullshit
    for (let i = 0; i < windows.length; i++) {
        let window = windows.item(i);
        // hide
        window.style.display = "none";
        // also makes the selector thingy
        let item = document.createElement("option");
        item.value = i;
        item.innerHTML = window.ariaLabel;
        // add it 
        dropdown.appendChild(item);
    }
}



