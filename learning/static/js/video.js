$(".full-screen").on("click",function(){
    document.querySelector(".video").requestFullscreen()
})
$(".mute").on("click",function(){
    document.querySelector(".video").muted=true
})
$(".volume-value").on("change",function(){
    var volume= parseInt(this.value)/100
    document.querySelector(".video").volume=volume
})
$(".play").on("click",function(){
    if( this.dataset.state == "pause"){
        $(".video")[0].play()
        this.innerHTML='<i class="fas fa-pause"></i>'
        this.dataset.state="play"
    }
    else{
        $(".video")[0].pause()
        this.innerHTML='<i class="fas fa-play"></i>'
        this.dataset.state="pause"
    }
    
})
$(".backplay").on("click",function(){
    v=document.querySelector(".video")
    v.currentTime = v.currentTime -5 
})
$(".volume-btn").on("click",function(){
    target=document.querySelector(".volume-options")
    console.log(target)
    if( $(target).css("visibility")  == "hidden" ){
        
        $(".volume-options").removeClass("hidden")
        $(".volume-options").addClass("visible")
    }
    else{
        
        $(".volume-options").removeClass("visible")
        $(".volume-options").addClass("hidden")
    }
})
$(".video").mouseover(function(){
    $(".buttons").css("visibility","visible")
      
})
$(".video").mouseleave(function(){
      
        $(".buttons").css("visibility","hidden")
        $(".volume-options").removeClass("visible")
        $(".volume-options").addClass("hidden")
      
})
$(".buttons").mouseover(function(){
    $(".buttons").css("visibility","visible")
      
})