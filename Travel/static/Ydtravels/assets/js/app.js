var App = function() {
		
    return {
		
		initGeneral : function()
		{

			jQuery('.carousel').carousel({
				interval: 10000,
				pause: 'hover'
			});

			jQuery('.top').click(function(){
				jQuery('html,body').animate({scrollTop: jQuery('body').offset().top}, 'slow');
			}); //move to top navigator

			jQuery('.tooltips').tooltip();	
			jQuery('.popovers').popover();

			jQuery(".fancybox-button").fancybox({
				prevEffect		: 'none',
				nextEffect		: 'none',
				closeBtn		: true,
				helpers		: {
					title	: { type : 'inside' }
				}
			});

			//fix html5 placeholder attribute for ie7 & ie8
			if (jQuery.browser.msie && jQuery.browser.version.substr(0,1) < 9) { // ie7&ie8
				jQuery('input[placeholder], textarea[placeholder]').each(function(){          
			        var input = $(this);        
			        
			        $(input).val(input.attr('placeholder'));
			                
			        $(input).focus(function(){
			             if (input.val() == input.attr('placeholder')) {
			                 input.val('');
			             }
			        });
			        
			        $(input).blur(function(){
			            if (input.val() == '' || input.val() == input.attr('placeholder')) {
			                input.val(input.attr('placeholder'));
			            }
			        });
			    });
			}
		},
    	   	
    	initInner : function() 
    	{
			
    	},

    	initProjects : function()
    	{
    		jQuery('.flexslider_single').flexslider({
		    	animation: "slide",
			    pauseOnHover: true,
			    directionNav: false,
			    count:2,
			    itemWidth: 385
			});
    	},

    	initMain : function()
    	{
    		jQuery('.flexslider').flexslider({
		    	animation: "slide",
			    animationLoop: true,
			    count:4,
			    pauseOnHover: true,
			    directionNav: false,
			    itemWidth: 292,
			    itemMargin: 0
			});
    	}
    	
    };
     
}();