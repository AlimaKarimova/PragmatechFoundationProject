/**let form=document.querySelector('form').innerHTML
function bosBuraxma(){
for(let i=0; i<form.length; i++)
if (form[i]!==0) {
   alert('sahe bos buraxila bimez')   
}
}**/

let birthday=document.getElementById('birthday').innerHTML
function birthdayTeyinEt() {
if (birthday<15) {
   alert('sizin 15 yasiniz yoxdur')
}
}
let a = document.getElementById('phone').innerHTML
function nomreniDuzgunYaz() {
   if (a!='+994') {
      alert('nomreni duzgun yaz')
   }
}




