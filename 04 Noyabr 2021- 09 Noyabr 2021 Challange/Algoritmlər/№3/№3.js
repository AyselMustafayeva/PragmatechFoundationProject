let a=Number(prompt("Enter your first number  : "))
let b=Number(prompt("Enter your  second number : "))

if(a>30 && a<70 && b>30 && b<70){
    document.write("Ikiside  30-70 arasında yerlewirler ")
}
else{
    if(a>30 && a<70 || b>30 && b<70){
        if(a>30 && a<70){
        document.write("Yalniz birinci dahil etdiyiniz "+a+" yerlewir 30-70 arasında ")
        }
        if(b>30 && b<70){
            document.write("Yalniz ikinci dahil etdiyiniz "+b+" yerlewir 30-70 arasında ")
            }
        }
    else{document.write("Hec biri yerlewmir")}
    
}