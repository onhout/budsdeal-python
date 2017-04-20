import "../less/order.less";
// var Feedback = require('../../globals/Feedback/Feedback.js').default;
var BudsChat = require('./buds_chat').default;

$(function () {
    var chat_pane = $('#order_chats');
    if (chat_pane.length >= 1) {
        new BudsChat(chat_pane.data('chatid'), chat_pane.data('sender'));
    }


    $('#id_item_amount').change(function () {
        var unit_price = parseFloat($(this).parents('tr').find('td.item_price').text());
        var value = parseFloat($(this).val());

        $(this).parents('tr').find('.order_subtotal').text(value * unit_price);

        $('#order_total').text(value * unit_price);
    });

    // function send_message() {
    //     socket.send($('#order_message').val())
    // }
    //
    // function reset_field(el){
    //     el.val('');
    // }
    //
    //
    // $('#send_order_message').click(function () {
    //     send_message();
    //     reset_field($('#order_message'))
    // });
    //
    // $('#order_message').on('keydown', function (e) {
    //     if (e.which == 13) {
    //         e.preventDefault();
    //         send_message();
    //         reset_field($(this))
    //     }
    // });
});