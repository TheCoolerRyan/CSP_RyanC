let images = ["https://cdnb.artstation.com/p/assets/images/images/003/940/707/large/robert-crescenzio-lightning-hydra-dc-dtf-robertcrescenzio-by-robertcrescenzio-dajsta9.jpg?1478737830","https://mythology.net/wp-content/uploads/2017/03/Dragon-Art.jpg","https://png.pngtree.com/png-clipart/20241014/original/pngtree-cute-little-dragon-png-image_16319539.png"]
document = newest_version_of_webpage.html
function show(){
    document.getElementById("hidden").style.display ="block"
} 
count = 0
function change(){
    document.getElementById("img").src= images[count]
    if(count === 2){
        count = 0
    }
    else{
        count +=1
    }
}