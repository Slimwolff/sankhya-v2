async function timer() {
    setTimeout(()=>{console.log("Timer disparado")}, 1000)
    return 0
}


async function callTimer() {
    console.log("Função iniciada...")
    console.log("chamando timer")
    let t = await timer()
    console.log(`timer executado e capturado em variavel -> ${t}`)
    console.log(`fim da função`)
}

callTimer()

function callJson() {
    fetch("http://example.com/api/articles/",{
        "headers": {
            "Content-Type": "application/vnd.api+json",
            // "Accept": "application/vnd.api+json"
        }
    }).then((data)=>{
        console.log(data.status)
        return data.json()

    }).then((n)=>{
        console.log(n)
    })
}

callJson()