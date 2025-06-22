
function randomColor() {
   // 16 הוא הבסיס ההקסדצימלי (hexadecimal), כלומר ספרות מ-0 עד F.
   // toString(16) ממיר את המספר למחרוזת בבסיס 16, כלומר לקוד צבע hex.
   return '#' + Math.floor(Math.random()*16777215).toString(16);
}

setInterval(()=>{
   document.body.style.backgroundColor = randomColor();
},1000)
