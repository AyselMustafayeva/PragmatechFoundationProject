class User{
    constructor(_ad,_yaw,_vezife){
        this.ad=_ad
        this.yaw=_yaw
        this.veife=_vezife
        console.log("Şəxsin adı: "+this.ad, " , Yawi: "+this.yaw, " , Vezife: "+this.veife)
    }
}
let user1= new User("Aysel","21","Student")
let user2 =new User("Ilon","50","milliarder")