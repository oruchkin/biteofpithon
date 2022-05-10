// When the user clicks the purchase button, render out
// "Something went wrong, please try again" in the paragraph
// that has the id="error".

let paragraph = document.getElementById("error")

console.log(paragraph)

function button_logic() {
    paragraph.innerHTML = "Something went wrong, please try again later"
}


