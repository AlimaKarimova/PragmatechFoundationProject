

let sectionHeight = document.querySelector('.header-nav-box').clientHeight

function changeNav() {
    if (window.scrollY > sectionHeight) {
       document.querySelector('.header-nav-box').className="bg-white"}
} 
