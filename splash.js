var splash = (function () {
    //for fading effect
    var img;
    var canvas;
    var ctx;
    var currentPixels = null;
    var fadespeed = 10;
    var white = false;
    var fadetimer;

    return {
	init: function() {
	    console.log("Initializing splash screen");
	    $("body").prepend('<img id="splash" src="images/Helping_Hand.jpg" />');
	    img = document.getElementById("splash");
	    canvas = document.createElement("canvas");
	    ctx = canvas.getContext("2d");
	    setTimeout(function() { splash.fade(2700, "images/StanfordLogo.jpg"); }, 500);
	},

	fade: function(time, nextimg) {
	    if (nextimg === "") {
		clearInterval(fadetimer);
		$("splash").remove();
	    }

	    canvas.width = img.width;
	    canvas.height = img.height;
	    
	    ctx.drawImage(img, 0, 0, 
			  img.naturalWidth, 
			  img.naturalHeight, 0, 0, img.width, img.height);
	    currentPixels = ctx.getImageData(0, 0, img.width, img.height);
	    
	    img.onload = null;
	    
	    fadetimer = setInterval(splash.changeColor, 100);
	    setTimeout(function() { splash.nextImage(nextimg); }, time);

	},

	changeColor: function() {
            for(var i = 0 ; i < currentPixels.data.length ; i++) {
                currentPixels.data[i]  += fadespeed;
            }

            ctx.putImageData(currentPixels, 0, 0);
            img.src = canvas.toDataURL("image/png");
	},

	nextImage: function(path) {
	    clearInterval(fadetimer);
	    img.src = path;
	    if (path !== "") {
		setTimeout(function() { splash.fade(2700, ""); }, 500);
	    }
	    else {
		setTimeout(main.init, 0);
	    }
	}
    }
})();
