

let save_elenemt = document.getElementById("save-el") 
let count_element = document.getElementById("count-el")
let count = 0



function increment() {
    //document.getElementById("count-el").innerHTML = count
    count += 1
    count_element.textContent = count
} 


function save() {
    let temp_counter = count + " - "
    save_elenemt.textContent += temp_counter
    count = 0
    count_element.textContent = count
    //console.log(count)
}

