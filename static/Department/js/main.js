$(document).ready(function () {
    $(".checkmark").on('change', function () {
        create_send_data(this)
    });

    $(".checkmark1").on('change', function () {
        create_send_data(this)
    });

    $(".checkmark2").on('change', function () {
        create_send_data(this)
    });
    $(".login100-form-btn").on('click', function () {

    });
});

$(document).ready(function () {
    $("#myInput").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#minimal-tbody tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

function create_send_data(object) {
    var row = $(object).parent().parent().parent();
    var reg_no = row.children(".reg_no").text();
    var pincode = row.children(".pincode").children().val();

    var attendance = row.children(".attendance").children().children().is(":checked");
    var year_back = row.children(".year_back").children().children().is(":checked");
    var category = row.children(".category").children().children().is(":checked");
    console.log(reg_no);
}

function load_data() {
    var course = document.getElementById("course").value;
    var verification = document.getElementById("verification").value;
    var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    console.log("load data function");
    console.log(course);
    console.log(verification);
    $.ajax("/department/getdata/", {
        method: "post",
        data: {
            course: course,
            verification_seniors: verification,
            csrfmiddlewaretoken: csrf,
        },

        success: function (data) {


            $("#minimal-tbody").html(data);


            $(".allotment_submit").on("click", function () {
                // var select = $($(this).parent().parent()).children(".rs-select2").children(".hostel").val();
                var reg = $($(this).parent().parent()).children(".reg_no").text();
                var pin = $($(this).parent().parent()).children(".pincode").children(".pin").val();
                var distance = $($(this).parent().parent()).children(".distance").children(".dist").val();
                var gender = $($(this).parent().parent()).children(".gender").children(".gender_desc").val();
                var yearofstudy = $($(this).parent().parent()).children(".yearofstudy").children(".yearofstudy_desc").val();
                var yearback = $($(this).parent().parent()).children(".year_back").children(".cont1").children(".year").is(":checked");
                var category = $($(this).parent().parent()).children(".category").children(".cont2").children(".category-inner").is(":checked");
                var prime = $($(this).parent().parent()).children(".prime").children(".prime_desc").val();
                var handicapped = $($(this).parent().parent()).children(".handicapped").children(".physically_desc").val();
                var keralaite = $($(this).parent().parent()).children(".keralaite").children(".keralaite_desc").val();
                var std_id = $($(this).parent().parent()).children(".std_id").text();
                console.log(distance);
                console.log(gender);
                console.log(keralaite);
                $.ajax("/department/savedata/", {
                    method: "post",
                    data: {
                        std_id: std_id,
                        reg: reg,
                        pin: pin,
                        gender: gender,
                        yearback: yearback,
                        category: category,
                        csrfmiddlewaretoken: csrf,
                        yearofstudy: yearofstudy,
                        handicapped: handicapped,
                        prime: prime,
                        nativity: keralaite,
                        distance: distance,
                    },
                });

            });
        }
    });
}

function changeColor(btn) {

    btn.style.backgroundColor = "#b5b3b2";

}

function priority() {
    console.log('a');
    var course = document.getElementById('course').value;
    var verification = document.getElementById('verification').value;
    var csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $.ajax('priority/', {
        method: 'post',
        data: {
            course: course,
            verification_seniors: verification,
            csrfmiddlewaretoken: csrf
        },
        success: function (data) {
            back_data = $("html").html();
            $("html").html(data)
        }
    });
}

function goback() {
    $.ajax('/department/', {
        method: 'get',

        success: function (data) {
            $("html").html(data)
        }
    });
}


