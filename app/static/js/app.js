(function($, document, window){
	

	$(document).ready(function(){

		(function($) {
			
			showSwal = function(type) {
			'use strict';
			if (type === 'auto-close') {
			swal({
			title: 'Auto close alert!',
			text: 'I will close in 2 seconds.',
			timer: 2000,
			button: false
			}).then(
			function() {},
			// handling the promise rejection
			function(dismiss) {
			if (dismiss === 'timer') {
			console.log('I was closed by the timer')
			}
			}
			)
			}else{
			swal("Error occured !");
			}
			}
			
			})(jQuery);

		// Cloning main navigation for mobile menu
		$(".mobile-navigation").append($(".main-navigation .menu").clone());

		// Mobile menu toggle 
		$(".toggle-menu").click(function(){
			$(".mobile-navigation").slideToggle();
		});

		var swiper = new Swiper('.swiper-container', {
			spaceBetween: 30,
			centeredSlides: true,
			autoplay: {
			  delay: 4500,
			  disableOnInteraction: false,
			},
			pagination: {
			  el: '.swiper-pagination',
			  clickable: true,
			},
			navigation: {
			  nextEl: '.swiper-button-next',
			  prevEl: '.swiper-button-prev',
			},
		  });
		

		$(".login-button").on("click",function(){
			$(".overlay").fadeIn();
			$(".auth-popup").toggleClass("active");
		});

		$(".close, .overlay").on("click",function(){
			$(".overlay").fadeOut();
			$(".popup").toggleClass("active");
		});

		initLightbox({
	    	selector : '.product-images a',
	    	overlay: true,
	    	closeButton: true,
	    	arrow: true
	    });


		$(document).keyup(function(e) {
			if( $(".popup").hasClass("active")){
		  		if (e.keyCode === 27) {
		  			$(".overlay").fadeOut();
					$(".popup").toggleClass("active");
		  		}   
			}
		});
	});

	$(window).load(function(){

	});










	
})(jQuery, document, window);