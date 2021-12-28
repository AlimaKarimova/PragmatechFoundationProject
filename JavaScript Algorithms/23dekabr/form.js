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
let birthday=document.getElementById('birthday').innerHTML
function birthdayTeyinEt() {
if (birthday<15) {
   alert('sizin 15 yasiniz yoxdur')
}
}


+
let email=document.querySelector('#email').innerHTML
function isareOlmalidi() {
 for (let i = 0; i < email.length; i++) 
 if (email[i]!='@') {
    alert('@ simvolumutleq olmalidi')
    
 }

}