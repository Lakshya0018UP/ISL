const but=document.getElementsByClassName("submit")

const inpu=document.getElementsByClassName("in")

but.onclick=(()=>{
    inpu.value=" "
    
})

const filled=document.querySelector(".filled");
function update(){
    filled.style.width=`${((window.scrollY)/(document.body.scrollHeight-window.innerHeight)*100)}%`
    requestAnimationFrame(update);
}
update();

