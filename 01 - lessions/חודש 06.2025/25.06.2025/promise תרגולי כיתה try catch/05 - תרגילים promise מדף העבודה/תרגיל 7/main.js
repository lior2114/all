function generateSngPasswordAsyntroc(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let password_size = 6;
            let chars = [
                'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M',
                'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '0','1','2','3','4','5','6','7','8','9'
            ]
            let password = []
            for (let i = 0; i < password_size; i++) {
                let index = Math.floor(Math.random() * chars.length)
                password.push(chars[index])
            }

            let hasLower = password.some(ch => ch >= 'a' && ch <= 'z')
            let hasUpper = password.some(ch => ch >= 'A' && ch <= 'Z')
            let hasDigit = password.some(ch => ch >= '0' && ch <= '9')
            if (hasLower && hasUpper && hasDigit) {
                resolve(password.join(''))
            } else {
                reject("Password must contain at least one lowercase letter, one uppercase letter, and one digit. your false password is: " + password)
            }
        }, 10);
    });
}


function random_password_activate(){
    let print_div = document.getElementById("result")
    generateSngPasswordAsyntroc()
    .then ((success) => {print_div.textContent = success})
    .catch((fail) => print_div.textContent =fail)
}