let equation = [];
let lastAnswer = undefined;

const findPercentage = () => {
    if(lastAnswer !== undefined){
        document.getElementById("display").setAttribute("value", `${eval(lastAnswer*100)}%`);
    }else{
        document.getElementById("display").setAttribute("value", `${eval(equation.join("")*100)}%`);
    }
}
const readValue = (number) => {
    if(number === "()"){
        if(equation.find((index) => index === "(")){
            equation.push(")");
            document.getElementById("display").setAttribute("value", equation.join(""));
        }else{
            equation.push("(");
            document.getElementById("display").setAttribute("value", equation.join(""));
        }
    }else{
        equation.push(number);
        document.getElementById("display").setAttribute("value", equation.join(""));
    }
}
const invertIndex = () => {
    let targetIndex = 0;
    let hasOperator = false;
    for(let i = equation.length-1; i > 0; i--){
        if(equation[i] === "*" || equation[i] === "/" || equation[i] === "-" || equation[i] === "+"){
            targetIndex = i;
            hasOperator = true;
            break;
        }
    }
    if(hasOperator){
        equation.splice(targetIndex+1, 0, "-");
        document.getElementById("display").setAttribute("value", equation.join(""));
    }else{
        equation.splice(0, 0, "-");
        document.getElementById("display").setAttribute("value", equation.join(""));
    }
}
const clearEquation = () => {
    equation = [];
    lastAnswer = undefined;
    document.getElementById("display").setAttribute("value", " ");
}   
const solveEquation = () => {
    if(eval(equation.join("")) !== undefined){
        document.getElementById("display").setAttribute("value", eval(equation.join("")));
        lastAnswer = eval(equation.join(""));
    }else{
        document.getElementById("display").setAttribute("value", "Error!");
    }
}
