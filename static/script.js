$(document).ready(function(){
	$(".loading").hide();
	$(".new_page_button").click(function(){
		$(".container-fluid").hide();
		$(".header2").hide();
		$(".header-main").show();
		$(".loading").show();
	});
	$(".assignment-type h4").click(function(){
		var $icon= $(this).children(".collapse-icon");
		if($icon.hasClass('icon-plus-sign'))
			$icon.removeClass('icon-plus-sign').addClass('icon-minus-sign');
		else
			$icon.removeClass('icon-minus-sign').addClass('icon-plus-sign');
		var $collapse= $(this).siblings('.collapse');
		$collapse.collapse('toggle');
	});    		
})