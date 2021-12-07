let userName = prompt('istifadeci adinizi daxil edin')
let userPassword = prompt('parolu daxil edin')

if (userName == 'admin'&& userPassword == '123456') {
   alert( 'Tebrikler siz sisteme daxil oldunuz');
   
}  else if (userName != 'admin' || userPassword != '123456') {
   alert('istifadeci adiniz ve ya parolunuz sehvdi')

}  else (userName == ''||userPassword == '') 
{
   alert('Deyerler bos ola bilmez');
}
   