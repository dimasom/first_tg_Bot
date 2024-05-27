import createObj from "./createObj.js"

export default async function createReq(HOST, name, pass) {
    await fetch(`${HOST}/registration`, {
        method: "POST",
        body: JSON.stringify(createObj(name, pass)),
        headers: {
            "Content-Type": "application/json",
        }
    })
}

export default async function getUsers(HOST) {
    const response = await fetch(`${HOST}/users`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    })
    const data = await response.json()
    console.log(data)
}
