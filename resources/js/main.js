$(document).ready(function(){
  
    $(window).scroll (function() {
        if ($(window).scrollTop()>685) {
            $('.navbar-dark').addClass('navbar-fixed-top');
        }
        if ($(window).scrollTop()<686) {
            $('.navbar-dark').removeClass('navbar-fixed-top');
    }
        
    });

    
    /* nav script */
    
    $(function() {
        $('a[href*="#"]:not([href="#"])').click(function() {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
              var target = $(this.hash);
              target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
              if (target.length) {
                $('html, body').animate({
                  scrollTop: target.offset().top -35
                }, 1000);
                return false;
              }
    }
  });
});
    
    
    
    
    
/*map*/    
    
    
var map = new GMaps({
  div: '.map',
  lat: 25.0339031,
  lng: 121.5623212
});    
    

map.addMarker({
  lat: 25.0339031,
  lng: 121.5623212,
  title: '101',
  infoWindow: {
  content: '<p>Taipei 101</p>'
}
});   
    
/*animate*/
    $('.js--wp-1').waypoint(function(direction){
        $('.js--wp-1').addClass('animated fadeIn');
    }, {
        offset:'50%'
    });
    
    $('.js--wp-2').waypoint(function(direction){
        $('.js--wp-2').addClass('animated fadeInLeft');
    }, {
        offset:'50%'
    });
    
    $('.js--wp-3').waypoint(function(direction){
        $('.js--wp-3').addClass('animated fadeInRight');
    }, {
        offset:'50%'
    });
    
    $('.js--wp-4').waypoint(function(direction){
        $('.js--wp-4').addClass('animated shake');
    }, {
        offset:'50%'
    });
    
    $('.js--wp-5').waypoint(function(direction){
        $('.js--wp-5').addClass('animated zoomInDown');
    }, {
        offset:'50%'
    });
    
    $('.js--wp-6').waypoint(function(direction){
        $('.js--wp-6').addClass('animated jello');
    }, {
        offset:'50%'
    });

    
    
});