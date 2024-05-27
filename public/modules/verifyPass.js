export default function verifyPassword(password) {
    let low = false
    let up = false
    let digit = false
    for(let elem of password) {
        if(/^[A-Z]$/.test(elem)) {
            up = true    
        } else if(/^[a-z]$/.test(elem)) {
            low = true
        } else if (/^\d+$/.test(elem)) {
            digit = true
        }  
    }if(up == true && low == true && digit == true && password.length >= 8) { 
        return true
    } else {
        return false
    }
    
}


