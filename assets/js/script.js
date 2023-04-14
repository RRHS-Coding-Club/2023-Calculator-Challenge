let equation = [];

function readInput(number){
    equation.push(number);
    document.getElementById("display").setAttribute("value", equation.join(" "));
}
function invertIndex(){
    let lastIndex = equation.length - 1;
    if(equation[lastIndex].charAt(0) != '-'){
        alert("Fuck");
    }else if(0 === 1){
    
    }else{

    }
}
function clearEquation(){
    equation = [];

}   
function solveEquation(){
    if(eval(equation.join(" ")) !== undefined){
        document.getElementById("display").setAttribute("value", eval(equation.join(" ")));
    }else{
        document.getElementById("display").setAttribute("value", "Error!");
    }
}