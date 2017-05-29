import "../less/user.less";
var Feedback = require('../../globals/Feedback/Feedback.js').default;
var Dialog = require('../../globals/Parts/Dialog').default;


$(function () {
    var feedback = new Feedback();

    var shipping_btn = $('#shipping_btn');
    if (shipping_btn.length > 0) {
        $.get('/user/shipping/add/', function (data) {
            var modal = new Dialog({
                id: shipping_btn.data('id'),
                modal_body: $(data),
            });
            modal.run_modal();
        });
        shipping_btn.attr('data-target', '#modal-' + shipping_btn.data('id'));
        shipping_btn.attr('data-toggle', 'modal');
    }
    shipping_btn.click(function (e) {
        e.preventDefault();
        $.get('/user/shipping/add/', function (data) {
            var modal = new Dialog({
                id: shipping_btn.data('id'),
                modal_body: $(data)
            });
            modal.run_modal();
        });
        shipping_btn.attr('data-target', '#modal-' + shipping_btn.data('id'));
        shipping_btn.attr('data-toggle', 'modal');
    });

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
            if (!$('#add_form').find('form').length) {
                $('#add_form').append(form)
            }
        })
    });
});