let xhttp = new XMLHttpRequest();



// Equivalent to <body onload="yourFunction();">
window.onload = function(){

    document.addEventListener('click', e => {
        const search = e.target.matches(".search-input")
        const dropdown = e.target.closest(".dropdown-menu")
        console.log(dropdown)
        if(!search && e.target.closest(".dropdown")!=null) return
 

    })
   
/* Event listener */
let search_input = document.querySelectorAll(".search-input")[0]
search_input.addEventListener('change',function(){
    console.log(search_input.value)
})


}
