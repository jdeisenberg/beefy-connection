
var width = 320;
var height = 0;
var streaming = false;

function show_canvas(){
	photo = $('div#photo_preview');	
	photo.removeClass('webcam');
	photo.html('<canvas id="canvas"></canvas><div id="img_preview"><img id="preview" alt="preview"></div>');
}

function show_webcam(){
	photo = $('div#photo_preview');
	photo.addClass('webcam');
	photo.html('<video id="video">Video not available.</video>');
}

function takepicture() {
	if (typeof $('canvas#canvas') === 'undefined'){
		show_canvas();
	}
	var canvas = $('canvas#canvas');
	var photo = $('img#preview');
	var context = canvas.getContext('2d');
	if (width && height) {
		canvas.width = width;
	    	canvas.height = height;
    		context.drawImage(video, 0, 0, width, height);
    		var data = canvas.toDataURL('image/png');
		photo.setAttribute('src', data);
	} else {
		clearphoto();
  	}
}

$(document).ready(function(){

  show_webcam();
  video = document.getElementById('video');

  navigator.getMedia = ( navigator.getUserMedia ||
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia ||
                         navigator.msGetUserMedia);

  navigator.getMedia(
    {
      video: true,
      audio: false
    },
    function(stream) {
      if (navigator.mozGetUserMedia) {
        video.mozSrcObject = stream;
      } else {
        var vendorURL = window.URL || window.webkitURL;
        video.src = vendorURL.createObjectURL(stream);
      }
      video.play();
    },
    function(err) {
      console.log("An error occured! " + err);
    }
  );

  $('button#btnTakePicture').click(function(e){
	e.preventDefault();
	if ($('div#user_preview').hasClass('webcam')){
		takepicture();
	}else{
		show_webcam();
	}
  });

});
