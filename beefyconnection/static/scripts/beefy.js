function fieldErr(obj,message){
	$(obj).addClass('red');
	$('<p class="error">' + message + '</p>').insertAfter($(obj));
}

function valAlpha(val){
	crit = /^[A-Za-z\.\,]+$/;
	if (!crit.test(val)){
		return false;
	}else{
		return true;
	}
}

function valText(val){
	crit = /^[A-Za-z0-9\. \?\!:\-(),@\u0080-\u00FF\u0100-\u017F\u0180-\u024F\u0370-\u03FF\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u0700-\u074F\u0900-\u097F\u0980-\u09FF\u0A00-\u0A7F\u0A80-\u0AFF\u0B00-\u0B7F\u0C00-\u0C7F\u0C80-\u0CFF\u0D00-\u0D7F\u0D80-\u0DFF\u0E00-\u0E7F\u0E80-\u0EFF\u0F00-\u0FFF\u1000-\u109F\u10A0-\u10FF\u1100-\u11FF\u1200-\u137F\u1700-\u171F\u1780-\u17FF\u1800-\u18AF\u4E00-\u9FFF\uAC00-\uD7AF\uF900-\uFAFF]+$/;
	if (!crit.test(val)){
		return false;
	}else{
		return true;
	}
}

function valEmail(val){
	crit = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	if (!crit.test(val)){
		return false;
	}else{
		return true;
	}
}

function valField(obj,func,message){
	var str = $(obj).val();
	if ((str != '') && (!func(str))){
		fieldErr($(obj),message);
	}
}

function valNum(val){
	crit = /^[0-9]+$/;
	if (!crit.test(val)){
		return false;
	}else{
		return true;
	}
}

function valPhone(val){
	crit = /^[\(\)\-0-9\+]+$/;
	if (!crit.test(val)){
		return false;
	}else{
		return true;
	}
}

function  validate(){
	$('p.error').remove();
	$('input').removeClass('red');
	$('.textval').each(function(){
		valField($(this),valText,'Please enter valid text.');
	});
	$('.alpha').each(function(){
		valField($(this),valAlpha,'Please enter only letters.');	
	});
	$('.email').each(function(){
		valField($(this),valEmail,'Please enter a valid email address.');	
	});	
	$('.number').each(function(){
		valField($(this),valNum,'Please enter only numbers.');	
	});
	$('.phone').each(function(){
		valField($(this),valPhone,'Please enter a valid phone numer.');	
	});
	$('.req').each(function(){
		if ($(this).val() == ''){
			$(this).addClass('red');
		}
	});
	success = true;
	$('input').each(function(){
		if ($(this).hasClass('red')){
			success = false;
		}
	});
	$('textarea').each(function(){
		if ($(this).hasClass('red')){
			success = false;
		}
	});
	return success;
}

function getData(){
	var interests = [];
	var data = {};
	$('input[name="interest"]').each(function(){
		if ($(this).is(':checked')){
			interests.push($(this).val());
		}
	});
	data['interests'] = interests;
	input_list = ['first-name','last-name','email','organization','irc','phone','address','city','state','postal','language','other_interest'];
	for(i=0;i<input_list.length;i++){
		if ($('input[name="' + input_list[i] + '"]').val() != ""){
			data[input_list[i]] = $('input[name="' + input_list[i] + '"]').val();
		}
	}
	if ($('textarea[name="comments"]').val() != ""){
		data['comments'] = $('textarea[name="comments"]').val();
	}
	console.log(data);
	return data;
}

function setupVideo() {
	navigator.getUserMedia = ( navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mozGetUserMedia ||
                       navigator.msGetUserMedia);

	if (navigator.getUserMedia) {
	navigator.getUserMedia (

		// constraints
		{
			video: true,
			audio: false
		},

		// successCallback
		function(localMediaStream) {
			var video = document.querySelector('video');
			video.src = window.URL.createObjectURL(localMediaStream);
			// Do something with the video here, e.g. video.play()
			video.play();
		},

		// errorCallback
		function(err) {
			console.log("The following error occurred: " + err);
			alert("The following error occurred: " + err);
		}
	);
	} else {
	console.log("getUserMedia not supported");
	alert("getUserMedia not supported");
	}
}

function takepicture() {
	// not using jQuery here; going "old school"
	var canvas = document.getElementById("photo_canvas");
	console.log(video.width + " " + video.height);
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    var data = canvas.toDataURL('image/jpeg');
    document.getElementById("photo_image").setAttribute('src', data);
  }

$(document).ready(function(){
	$('div#interests').hide();

	if ($('img#logo').attr('src') == '$(logo)'){
		$('img#logo').hide();
	}
	
	$('button').click(function(e){
		e.preventDefault();
	});
	
	$('button#next').click(function(){
		if (validate()){
			$('div#contacts').hide();
			$('div#interests').show();
		}
	});

	$('button#back').click(function(){
		$('div#contacts').show();
		$('div#interests').hide();
	});
	
	$('button#submit').click(function(){
		if(validate()){
			data = getData();
			$.ajax({
				url:'/bc-post',
				method: 'POST',
				data: data,
				dataType: 'json',
			}).done(function(result){
				if (result.status != 'error'){
					img = $('img#photo_image');
                			if (typeof img !== 'undefined'){
                        			$.ajax({
                                		url:'/bc-upload',
                                		method: 'POST',
                                		enctype: 'multipart/form-data',
                                		dataType: 'json',
                               			data: { 'photo' : img.attr('src') },
                                		}).done(function(result){
							window.location.replace('/bc-success');
                                		});
                			}
				}else{
					alert("Couldn't submit your form.  " + result.message);
				}
			});
		}
	});

	setupVideo();
	
	$('button#btnTakePicture').click(function(){
      takepicture();
	});
});
