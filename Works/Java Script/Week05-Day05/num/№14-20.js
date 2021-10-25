let nums=[1,2,3,6,7,8,23,78,34,12];
let a=0;
let nums3 =[];
let tek=[];
//birinci mesele
for(let i=0;i<nums.length;i++){
a+=nums[i]
}
console.log(a)   //Ədədlərin cəmini tapan metod yazın

//ikinci mesele
nums.sort(function(a,b){return b-a})
console.log(nums)   //Ədədlərin böyükdən kiçiyə doğru sıralayın

//dorduncu mesele 
for(let n=0;n<nums.length;n++){
    nums3.push(nums[n]*nums[n])
}
console.log(nums3)    //Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın

//yeddinci mesele 
for(let q=0;q<nums.length;q++){
    if(nums[q]%2==1){
        tek.push(nums[q]);
    }
}
console.log(tek)       //Tək ədədləri ayıraraq ayrıca bir massivə yığan metod yazın

