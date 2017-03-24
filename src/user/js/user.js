import "../less/user.less";
// const fbButton = $('#facebookButton');
// const googButton = $('#googleButton');
// var FB = require('../../globals/Facebook/Button').default;
// var GOOGLE = require('../../globals/Google/Button').default;
// fbButton.append(FB.register(fbButton.data('method')));
// googButton.append(GOOGLE.register(googButton.data('method')));


$(function () {
    $('#toggle-sidebar').click(function () {
        $('#cross').toggle();
        $('#bars').toggle();
        $('#wrapper').toggleClass('toggled');
    });
    //file upload
    $(".js-upload-photos").click(function () {
        $("#id_image").click();
    });

    /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
    $("#id_image").fileupload({
        dataType: 'json',
        done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
            if (data.result.is_valid) {
                $("#gallery tbody").prepend(
                    "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
                )
            }
        }
    });
});