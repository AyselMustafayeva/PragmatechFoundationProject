
function il(a){
    if(a%400==0){
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
console.log(il(3000) + " ve 12 ay")