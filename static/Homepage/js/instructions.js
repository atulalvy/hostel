// ======== navbar ===========


(function ($) {
    'use strict';

    var activeItem = $('.bez.active1');
    var activeWidth = $(activeItem).innerWidth();
    var activeHeight = $(activeItem).outerHeight();
    var itemPos = $(activeItem).position();
    $(".selector").css({
        "left": itemPos.left + "px",
        "width": activeWidth + "px",
        "height": activeHeight + "px",
        "top": itemPos + "px"
    });
    $(".selector").append($(".active1").clone());


    $(".bez").on("click", function (e) {

        $('.bez').removeClass("active1");
        $(this).addClass('active1');
        $(".selector").empty()
        var activeWidth = $(this).outerWidth();
        var itemPos = $(this).position();
        var activeHeight = activeItem.outerHeight();
        $(".selector").css({
            "left": itemPos.left + "px",
            "height": activeHeight + "px",
            "width": activeWidth + "px",
            "top": itemPos.top + "px"
        });
        $(".selector").append($(".active1").clone())
    });

    function toggle() {
        $(".selector").empty()

        var activeWidth = $(".active1").outerWidth();
        var itemPos = $(".active1").position();
        var activeHeight = activeItem.outerHeight();
        $(".selector").css({
            "left": itemPos.left + "px",
            "height": activeHeight + "px",
            "width": activeWidth + "px",
            "top": itemPos.top + "px"
        });
        $(".selector").append($(".active1").clone())
    }

    setInterval(toggle, 400)

    $('.navbar-toggler').on('click', function () {
        setTimeout(toggle, 500)
    })

    $(window).on("resize", function (e) {
        e.preventDefault();
        $(".selector").empty()

        var activeWidth = $(".active1").outerWidth();
        var itemPos = $(".active1").position();
        var activeHeight = activeItem.outerHeight();
        $(".selector").css({
            "left": itemPos.left + "px",
            "height": activeHeight + "px",
            "width": activeWidth + "px",
            "top": itemPos.top + "px"
        });
        $(".selector").append($(".active1").clone())
    })

})(jQuery);