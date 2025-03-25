function pyramid(rowNumber) {
    let n = "#"
    let r = []
    for(let x = 0; x <= rowNumber; x++) { 
        for(let i = rowNumber; i >= 0; i--){
            let a = n.repeat(i)
            r.unshift(a)
        }
    }
    return r
}

console.log(pyramid(8));
