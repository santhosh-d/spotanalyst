
//Scroll to change Navbar's Background

$(window).on('scroll', function () {
    if ($(window).scrollTop()) {
        $('nav').addClass('scroll');
        $('.logo_desc').hide();
    }
    else {
        $('nav').removeClass('scroll');
        $('.logo_desc').show();
    }
})
//Switch Active Classes Js
$(document).on('click','ul li a',function(){
  $('ul li a').removeClass('active')
  $(this).addClass('active')
})


//Smooth Scroll
$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});