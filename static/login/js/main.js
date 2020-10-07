$(document).ready(function () {
    $("input").on('click', function () {
        this.parentNode.classList.remove("alert-validate")
    })
});


document.getElementById("log_btn").onclick = function () {
    document.getElementById("Login").style.display = "block";
    document.getElementById("SignUp").style.display = "none";
    document.getElementById("log_btn").style.color = "black";
    document.getElementById("reg_btn").style.color = "#8f8e8d";

};
document.getElementById("reg_btn").onclick = function () {

    document.getElementById("Login").style.display = "none";
    document.getElementById("SignUp").style.display = "block";
    document.getElementById("log_btn").style.color = "#8f8e8d";
    document.getElementById("reg_btn").style.color = "black";


};


function hashing(event) {

    var raw1 = document.getElementById('id_password1').value;
    var raw2 = document.getElementById('id_password2').value;
    var username = document.getElementById('username').value;

    var tag = document.getElementsByTagName('input');
    for (i = 0; i < tag.length; i++) {

        tag[i].parentNode.classList.remove("alert-validate");
    }

    document.getElementById('RegistrationForm').setAttribute("isvalid", "true");

    var regex = /^(.{0,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{4,})|(.{1,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{3,})|(.{2,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{2,})|(.{3,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{1,})|(.{4,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{0,})$/;
    var email_regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (email_regex.test(username)) {
        if (regex.test(raw1)) {
            if (raw1 !== raw2) {
                document.getElementById('id_password2').parentNode.classList.add("alert-validate");
                document.getElementById('id_password2').parentNode.setAttribute('data-validate', 'Passwords must be same');
                event.preventDefault();
            } else {
                document.getElementById('id_password1').value = sha512(raw1);
                document.getElementById('id_password2').value = sha512(raw2);
                document.getElementById('RegistrationForm').submit()
            }

        } else {
            document.getElementById('id_password1').parentNode.classList.add("alert-validate");

            document.getElementById('id_password1').parentNode.setAttribute('data-validate', 'Password Must be atleast 8 characters long, must include atleast a character  and a digit or special characters');
            event.preventDefault();
        }
    } else {
        document.getElementById('username').parentNode.classList.add("alert-validate");

        document.getElementById('username').parentNode.setAttribute('data-validate', 'Input must be a valid email');
        event.preventDefault();
    }
}

function hashing1(event) {
    var raw1 = document.getElementById('id_password').value;
    document.getElementById('id_password').value = sha512(raw1);
    // console.log(sha512(raw1));


}


function hashing2(event) {

    var raw1 = document.getElementById('id_password1').value;
    var raw2 = document.getElementById('id_password2').value;

    var tag = document.getElementsByTagName('input');
    for (i = 0; i < tag.length; i++) {

        tag[i].parentNode.classList.remove("alert-validate");
    }

    document.getElementById('RegistrationForm').setAttribute("isvalid", "true");

    var regex = /^(.{0,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{4,})|(.{1,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{3,})|(.{2,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{2,})|(.{3,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{1,})|(.{4,}(([a-zA-Z][^a-zA-Z])|([^a-zA-Z][a-zA-Z])).{0,})$/;
    if (regex.test(raw1)) {
        if (raw1 !== raw2) {
            document.getElementById('id_password2').parentNode.classList.add("alert-validate");
            document.getElementById('id_password2').parentNode.setAttribute('data-validate', 'Passwords must be same');
            event.preventDefault();
        } else {
            document.getElementById('id_password1').value = sha512(raw1);
            document.getElementById('id_password2').value = sha512(raw2);
            document.getElementById('RegistrationForm').submit()
        }

    } else {
        document.getElementById('id_password1').parentNode.classList.add("alert-validate");

        document.getElementById('id_password1').parentNode.setAttribute('data-validate', 'Password Must be atleast 8 characters long, must include atleast a character  and a digit or special characters');
        event.preventDefault();
    }
}


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