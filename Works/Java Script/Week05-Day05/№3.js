
function il(a){
    if(a%1000==0){
        return "366 day"
    }
    else{
        if(a%100==0){
            return "365 day"
        }
        else{
            if(a%4==0){
                return "366 day"
            }
            else{
                return "365 day"
            }
        }
    }
}
console.log(il(1616))