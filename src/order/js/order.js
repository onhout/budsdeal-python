import "../less/order.less";
// var Feedback = require('../../globals/Feedback/Feedback.js').default;

$(function () {
    if ($('.order_message_container').length >= 1) {
        var socket = new WebSocket("ws://" + window.location.host + "/chat?order_id=" +
            $('.order_message_container').data('chatid'));

        socket.onmessage = function (e) {
            $('.order_message_container').append(e.data)
        };

        // Call onopen directly if socket is already open
        if (socket.readyState == WebSocket.OPEN) socket.onopen();

    }


    $('#id_item_amount').change(function () {
        var unit_price = parseFloat($(this).parents('tr').find('td.item_price').text());
        var value = parseFloat($(this).val());

        $(this).parents('tr').find('.order_subtotal').text(value * unit_price);

        $('#order_total').text(value * unit_price);
    });


    $('#send_order_message').click(function () {
        socket.send("hello world");
    })
});