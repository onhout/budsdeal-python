import "../less/user.less";
// const fbButton = $('#facebookButton');
// const googButton = $('#googleButton');
// var FB = require('../../globals/Facebook/Button').default;
// var GOOGLE = require('../../globals/Google/Button').default;
// fbButton.append(FB.register(fbButton.data('method')));
// googButton.append(GOOGLE.register(googButton.data('method')));
var Image_Upload = require('./file_upload').default;


$(function () {
    $('#toggle-sidebar').click(function () {
        $('#cross').toggle();
        $('#bars').toggle();
        $('#wrapper').toggleClass('toggled');
    });

    $('.js-upload-photos').click(function () {
        new Image_Upload('#id_image');
    });


    $('.delete_photo').click(function (e) {
        var ID = $(this).data('image_id');
        return Image_Upload.deleteFN(ID, $(this).data('csrftoken'), $(this))(e)
    })
});