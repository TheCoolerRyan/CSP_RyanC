let images = ["https://www.earthdiver.com/cdn-cgi/image/width=4000,quality=75,format=auto/https://assets.earthdiver.com/media/media-2727684.jp?w=5246&h=2193&tick=1667491652923","https://images.squarespace-cdn.com/content/v1/63c60d44c98af85334537583/644359f9-c213-4d77-bdb0-b78b7f8424f3/Mount_Timpanogos_at_sunset.jpg","https://www.nicodebarmore.com/wp-content/uploads/2014/08/wildflower-basin-1024x1020.jpg"]
document = notes.html
function hello(){
    let name = window.prompt("What is your name?","Koro Sensei")
    document.getElementById("title").
    innerHTML = "Hello " + name + "!"

}
count = 0
function change(){
    document.getElementById("img").src= images[count]
    if(count === 2){
        count = 0
    }else{
        count +=1
    }
}
function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("btn").style.color = "white"
}
function normal(){
    document.getElementById("btn").style.backgroundColor="gray"
    document.getElementById("btn").style.color = "black"
}
function push(){
    document.getElementById("btn").style.backgroundColor="red"
}
function show(){
    document.getElementById("hidden").style.display = "block"
}
function pop(){
    window.alert("For real. Don't click this!")
}
/*use in final */

function more(){
    if(document.getElementById("extra").style.display != "flex"){
        document.getElementById("extra").style.display = "flex"
        document.getElementById("shw").innerHTML ="Show Less"
    }else{
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML ="Show More"
    }
    
}