import "../less/products.less";
var Feedback = require('../../globals/Feedback/Feedback.js').default;

var Image_Upload = require('./file_upload').default;

$(function () {

    $('.js-upload-photos').click(function () {
        if (!$(this).hasClass('disabled')) {
            new Image_Upload('#id_image');
        }
    });


    $('.delete_photo').click(function (e) {
        var ID = $(this).data('image_id');
        return Image_Upload.deleteFN(ID, $(this).data('csrftoken'), $(this))(e)
    });

    $('.make_primary_photo').click(function (e) {
        var ID = $(this).data('image_id');
        return Image_Upload.makePrimaryPhoto(ID, $(this).data('csrftoken'), $(this))(e)
    });

    var feedback = new Feedback();
});