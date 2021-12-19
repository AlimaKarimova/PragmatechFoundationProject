
function changeBg(){
 document.body.style.background = 'red'  
}


function changeTitleColor(){
   document.querySelector('h1').style.color = 'green'
} 


function changeTextColor(){
   document.querySelector('ul').style.color = 'yellow'
}

function cerciveElaveEt(){
document.querySelector('img').style.border= 'thick solid yellow'
}

function sekliDeyis(){
   document.getElementById('image').src= '/Algorithms/18dekabr/g83rrbcpsylwwxn9p92q.jpg'
}

function countSayHerf(){
   let a = document.querySelector('.metn').innerHTML.length
   let b = document.querySelector('.netice').innerHTML
   document.querySelector('.netice').innerHTML = b + a
}

function proqramciSozunuTap(){
let a = document.querySelector('.tovsiyeler').innerHTML.includes('Proqramçı')
let b = document.querySelector('.netice').innerHTML
if (a = true) {
   document.querySelector('.netice').innerHTML = b + 'var'
} else{
   document.querySelector('.netice').innerHTML = b + 'yoxdur'
}
}

function yeriniDeyis(){
   document.querySelector('.ul.li').innerHTML.reverse()
}