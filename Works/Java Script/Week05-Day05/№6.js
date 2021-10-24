let age=[17,19,18,20,25,22];
function qruppa(){
    let newage=[]
    for(let i=0;i<6;i++){
       newage.push(age[i]*2);
    }
    return newage;
}
console.log(qruppa())