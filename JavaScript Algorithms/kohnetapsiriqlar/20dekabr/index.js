

const minute = 1000 * 60;
const hour = minute * 60;
const day = hour * 24;
const year = day * 365;

let d = new Date(1992, 04, 22, 00, 00, 00, 00);
let years = Math.round(Date.now() / year);
document.querySelector("p").innerHTML = years;
