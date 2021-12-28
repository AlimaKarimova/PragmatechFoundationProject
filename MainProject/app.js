let animation= document.querySelectorAll('.left')
function createAnimation() {
   animation.style.left=`-200px`
}

let education = document.querySelector('.education').clientWidth

function getAnimation() {
   if (window.scrollX > education) {
       createAnimation()
   }
} 