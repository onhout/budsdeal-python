import "../less/user.less";
var Feedback = require('../../globals/Feedback/Feedback.js').default;
var Dialog = require('../../globals/Parts/Dialog').default;


$(function () {


    var feedback = new Feedback();


    var shipping_btn = $('#shipping_btn');
    $.get('/user/shipping/add/', function (data) {
        var modal = new Dialog('Add A Shipping', '', '', shipping_btn.data('id'));
        modal.modal_body = $(data);
        modal.save_text = 'Submit';
        modal.run_modal();
    });
    shipping_btn.attr('data-target', '#modal-' + shipping_btn.data('id'));
    shipping_btn.attr('data-toggle', 'modal');

    $('.edit_shipping').click(function (e) {
        e.preventDefault();
        $.get($(this).data('url'), function (data) {
            var form = $(data).append($('<button/>', {
                'class': 'btn btn-primary btn-raised',
                'text': 'Submit'
            }).click(function () {
                $.ajax({
                    type: "POST",
                    url: form.attr('action'),
                    data: form.serialize(),
                    success: function (data) {
                        if (data.status == 'success') {
                            location.reload()
                        } else {
                            alert('An error occurred')
                        }
                    }
                });
            })).append($('<a/>', {
                'class': 'btn btn-danger btn-raised',
                'text': 'Close'
            }).click(function () {
                form.remove()
            }));

            $('#add_form').append(form)
        })
    });
});