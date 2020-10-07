$(document).ready(function () {
    // Transition effect for navbar
    $(window).scroll(function () {
        // checks if window is scrolled more than 500px, adds/removes solid class
        if ($(this).scrollTop() > 500) {
            $('.navbar').addClass('solid');
        } else {
            $('.navbar').removeClass('solid');
        }
    });
});

"use strict";
$(document).ready(function () {
    new Swiper(".swiper-container", {
        initialSlide: 1,
        spaceBetween: 0,
        // speed: 100,
        loop: 1,
        effect: "coverflow",
        coverflow: {
            rotate: 0,
            stretch: 600,
            depth: 50,
            modifier: 1,
            slideShadows: !1
        },

        autoplay:true,
        speed:2000,

        slidesPerView: 2,
        slideToClickedSlide: !0,
        pagination: ".swiper-pagination",
        nextButton: ".swiper-button-next",
        prevButton: ".swiper-button-prev",
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 0,
                coverflow: {
                    rotate: 0,
                    stretch: 100,
                    depth: 200,
                    modifier: 1,
                    slideShadows: !1
                },
            },
            600: {
                slidesPerView: 1,
                spaceBetween: 0,
                coverflow: {
                    rotate: 0,
                    stretch: 600,
                    depth: 50,
                    modifier: 0,
                    slideShadows: !1,
                    slidesPerView:1
                },
            },
        }
    });

})
;
