$(document).ready(function() {
	var h = window.innerHeight;
	var w = window.innerWidth;
	$('.first').css('height', h / 1.05);
	$('.second').css('height', h);
	$('#blue-right').css('height', h);
	$('#blue-right').css('width', w / 2);

	$('#link-input').focus(function() {
		$(this).val('');
	});

	$('#logo').click(function() {
		window.location = '/rate/';
	});

	// $('b').click(function() {
	// 	var li = $(this).parent();
	// 	if (li.hasClass('li-active')) {
	// 		li.removeClass('li-active');
	// 	} else {
	// 		$('li').removeClass('li-active');
	// 		li.addClass('li-active');
	// 	}
	// });

});