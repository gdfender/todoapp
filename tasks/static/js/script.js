$(document).ready(function () {
	$(document).on('click', '.remove', function() {
		$(this).parent().addClass('completed');
		$(this).attr('disabled', true);
	});

	$(document).on('click', '.checked', function(){
		$(this).parent().remove();
	});

});