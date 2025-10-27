
function hrefs() {
     const all = document.getElementsByClassName("href-btn");

    for (let i = 0; i < all.length; i++) {
        let item = all.item(i)
        if (item.ariaDisabled == "true") {
            console.log(item + " disabled")
        } else {
        item.addEventListener("click", function() {
            window.location.href = item.ariaLabel;
            
            
        })

        }

    }   
}

function downloads() {
    const all = document.getElementsByClassName("download-btn");

    for (let i = 0; i < all.length; i++) {
        let item = all.item(i)
        if (item.ariaLabel == "#") {
            console.log(item + " disabled")
        } else {
        item.addEventListener("click", function() {
            let wind = window.open(item.ariaLabel);
            setTimeout(() => {
                wind.close()
            }, 3000);
            
             
        })

        }

    }   
}

hrefs();
downloads();

