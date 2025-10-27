

fullscreenButtons();
closeButtons();


// adds fullscreen functionality which is 
function fullscreenButtons() {
    
    const btns = document.getElementsByClassName("fullscreen");

    for (let is = 0; is < btns.length; is++) { {
        let item = btns.item(is);

        item.addEventListener("click", function redir() {
            let win = window.open(item.dataset.fs);
            
        })
    }
    }
}

function closeButtons() {
    // ...
    const closeButtonElements = document.getElementsByClassName("close");


    for (let ia = 0; ia < closeButtonElements.length; ia++) {
        let closebtn = closeButtonElements.item(ia);

        closebtn.addEventListener("click", function closee() {
            // i fucking hate myself for writing this snippet of close
            // -enorsu 2025
            closebtn.parentElement.parentElement.parentElement.style.display = "none";
            
        })
    }
}