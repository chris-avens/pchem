function gasLaw(P, V, T, formula) {
    const formulaArr = {
        ideal: {
            P: () => {return 8.314 * T / V},
            V: () => {return 8.314 * T / P},
            T: () => {return P * V / 8.314},
        }
    }
    index = !P ? 'P' : !V ? 'V' : 'T';
    console.log(formula, index, P, V, T)
    return formulaArr[formula][index]()
}

console.log(gasLaw(3, 5, null, 'ideal'))