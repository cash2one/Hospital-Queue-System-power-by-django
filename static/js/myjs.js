$('#weibo').click(function(e){
	var $me = $(this), interval;
	
	e.preventDefault();
	
    $me.grumble({
		text: '我们的微博账号是',
		angle: 20,
		distance: 2,
		showAfter: 0,
		hideAfter: false,
		hasHideButton: true,
		type: 'alt-', 
	});
});

$('#weixin').click(function(e){
	var $me = $(this), interval;
	
	e.preventDefault();
	
    $me.grumble({
		text: '我们的公众微信平台是',
		angle: 20,
		distance: 3,
		showAfter: 0,
		hideAfter: false,
		hasHideButton: true,
		type: 'alt-', 
	});
});

$('#ambulance').click(function(e){
	var $me = $(this), interval;
	
	e.preventDefault();
	
    $me.grumble({
		text: '我们的紧急求助电话是',
		angle: 20,
		distance: 3,
		showAfter: 0,
		hideAfter: false,
		hasHideButton: true,
		type: 'alt-', 
	});
});


