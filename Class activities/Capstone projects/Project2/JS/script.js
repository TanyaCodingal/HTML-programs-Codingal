const btn=document.getElementById("themeBtn");
btn.addEventListener("click",()=>{
    document.body.classList.toggle("dark-mode");
    if(document.body.classList.toggle("dark-mode")){
        btn.innerHTML='<i class="bi bi-sum-fill"></i>';
    }
    else{
        btn.innerHTML='<i class="bi bi-mon-stars-fill"></i>'
    }

})

let cartCount=0;
document.querySelectorAll(".addClick").forEach(button=>{
    button.addEventListener("click",function(){
        cartCount++;
        document.getElementById("cartCount").innerHTML=cartCount;
        alert("Item added to your Cart")
    })
})