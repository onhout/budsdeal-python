import "../less/order.less";
// var Feedback = require('../../globals/Feedback/Feedback.js').default;
var BudsChat = require('./buds_chat').default;
var Dialog = require('../../globals/Parts/Dialog').default;

$(function () {
    var chat_pane = $('#order_chats');
    if (chat_pane.length >= 1) {
        var chat = new BudsChat(chat_pane.data('chatid'), chat_pane.data('sender'));
    }

    $('#id_item_amount').change(function () {
        var unit_price = parseFloat($(this).parents('tr').find('td.item_price').text());
        var value = parseFloat($(this).val());

        $(this).parents('tr').find('.order_subtotal').text(value * unit_price);
        $('#order_total').text(value * unit_price);
    });

    var finalize_btn = $('#finalize-order');
    finalize_btn.click(function (e) {
        e.preventDefault();
        $(this).attr('data-target', '#modal-' + $(this).data('id'));
        new Dialog('Finalize',
            'Are you sure you want to finalize the order?',
            $(this).data('url'),
            $(this).data('id'));
    });
    finalize_btn.attr('data-toggle', 'modal');

});