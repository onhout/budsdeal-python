import "../less/order.less";
// var Feedback = require('../../globals/Feedback/Feedback.js').default;

$(function () {
    $('#id_item_amount').change(function () {
        var unit_price = parseFloat($(this).parents('tr').find('td.item_price').text());
        var value = parseFloat($(this).val());

        $(this).parents('tr').find('td.order_subtotal').text('$' + value * unit_price);

        $('#order_total').text('$' + value * unit_price);
    });
});