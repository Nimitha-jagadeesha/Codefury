$(document).ready(function(){ 
    $('.wrapper').slideDown('slow'); 
    $('#navButton').click(function(){
        $('.menu').slideToggle('slow');
      togglemenu();
    });
});

function togglemenu() {
var div = document.getElementById("navButton");
  
if (div.className == "closed") {open();}
else{close();}
}

function open() {
document.getElementById("navButton").innerHTML="- Close -   <div class=\"bar left\"></div><div class=\"bar top\"></div><div class=\"bar right\"></div><div class=\"bar bottom\"></div>";
document.getElementById("navButton").className = "open";
}

function close() {
document.getElementById("navButton").innerHTML="- Menu - <div class=\"bar left\"></div><div class=\"bar top\"></div><div class=\"bar right\"></div><div class=\"bar bottom\"></div>";
document.getElementById("navButton").className="closed";
}

//gallery stuff

$(".galleryItem").mouseenter(function() {
  var thisoverlay = $(this).find('.galleryOverlay');
  
  thisoverlay.stop(true, true).animate({
    height: '200',
    marginTop: '-230px'
  });
});

$(".galleryItem").mouseleave(function() {
  var thisoverlay = $(this).find('.galleryOverlay');
  
  thisoverlay.stop(true, true).animate({
    height: '20',
    marginTop: '-45px'
  });
});