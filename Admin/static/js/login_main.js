;(function () {
	'use strict';
    //var a = function () {
    //$("#login").click(function () {
    //    var user = $("#Username").val();
    //    var pwd = $("#Password").val();
    //    var pd = {"username": user, "password": pwd};
    //    $.ajax({
    //        type: "post",
    //        url: "/",
    //        data: pd,
    //        cache: false,
    //        success: function (data) {
    //            window.location.href = "/auth/login?user=" + data;
    //        },
    //        error: function () {
    //            alert("error!");
    //        }
    //    });
    //});};
	// Placeholder
	var placeholderFunction = function() {
		$('input, textarea').placeholder({ customClass: 'my-placeholder' });
	};

	// Placeholder
	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated-fast') ) {

				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn animated-fast');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft animated-fast');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight animated-fast');
							} else {
								el.addClass('fadeInUp animated-fast');
							}

							el.removeClass('item-animate');
						},  k * 200, 'easeInOutExpo' );
					});

				}, 100);

			}

		} , { offset: '85%' } );
	};
	// On load
	$(function(){
		placeholderFunction();
		contentWayPoint();
        //a();
	});

}());
