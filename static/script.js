$(document).ready(function(){
	$(".loading").hide();
	$(".new_page_button").click(function(){
		$(".container-fluid").hide();
		$(".header2").hide();
		$(".header-main").show();
		$(".loading").show();
		startEllipsis();
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
/*
 * animated ellipsis
 * 
 * Created by Torsten Walter on 2008-04-06.
 * Copyright playground.magicrising.de. Some rights reserved.
 *
 * This script may be copied and reproduced
 * if this copyright notice is left intact.
 */

ellipsis = ['', '.', '..', '...'];
var runEllipsis = false;
function animateEllipsis(el, count) {
	el.innerHTML = ellipsis[count%4];
	if(runEllipsis == true) {
	 window.setTimeout( function(){
	   animateEllipsis(el, ++count);}, 250);
	}
}
function startEllipsis() {
	runEllipsis = true;
	animateEllipsis(document.getElementById('ellipsisSpan'), 0);
}
function stopEllipsis() {
	runEllipsis = false;
}