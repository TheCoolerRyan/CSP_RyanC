let images = ["https://th-thumbnailer.cdn-si-edu.com/prCcoKOQiPkBi5QvIyWHEQVIltE=/fit-in/1600x0/https://tf-cmsv2-journeys-media.s3.amazonaws.com/filer/d2/52/d252f665-21c6-4daa-b163-8911ddd0d383/ut_bryce_hoodoos_sunset_ist_176984017.jpg","https://i0.wp.com/www.brycecanyoncountry.com/wp-content/uploads/bryce-canyon-national-park_bestcamping2_5132d5d4.webp","https://npf-prod.imgix.net/uploads/Bryce_iStock_0000030624082028229.jpg?auto=compress%2Cformat&fit=max&q=80&w=1600"]



let num=0

function change(){
    document.getElementById("image").src = images[num]
    if(num ===2){
        num = 0
    }else{
        num += 1
    }

}
function more(){
    if(document.getElementById("extra").style.display != "flex"){
        document.getElementById("extra").style.display = "flex"
        document.getElementById("shw").innerHTML ="Show Less"
    }else{
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML ="Show More"
    }
    
}