import verifyPassword from "./modules/verifyPass.js"
import createReq from "./modules/createRequest.js"
import getUsers from './modules/createRequest.js'
import URL from "./config.js"
const $name = document.querySelector('.name')
const $pass = document.querySelector('.pass')


async function registrationClickHandler(event) {
    event.preventDefault()
    try {
        if(verifyPassword($pass.value)) {
            createReq(URL, $name.value, $pass.value)
        } else {
            alert('Недопустимый пароль')
        }
    }
    catch (e) {
        console.error(e)
        alert('Произошла ошибка при запросе! ')
    }

}


const $btn = document.querySelector('.btn')
$btn.addEventListener('click', registrationClickHandler)



document.addEventListener('DOMContentLoaded', getUsers)
