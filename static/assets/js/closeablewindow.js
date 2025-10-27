
// get the close button
const closeBtn = document.getElementById("close");


// 🤫
let count = 0;
const titlebartext = document.getElementsByClassName("title-bar-text")[0];
const oldtext = titlebartext.innerHTML;
titlebartext.addEventListener("click", goosesate);
// 🤫
function goosesate() {
    if (count == 44) {
        titlebartext.innerHTML = "why did you click me 44 times"
    } else if (count == 45) {
        titlebartext.innerHTML = oldtext;
    } else if (count == 88) {
        let shark = window.open("/pages/shark");
        setTimeout(() => {
            shark.close();
        }, 333)
    }
    count++;

}

// fn
function closeWindow() {
    // get window
    const window = document.getElementById("window");
    window.style.display = "none";
}

// insert eventlistener
closeBtn.addEventListener('click', closeWindow);