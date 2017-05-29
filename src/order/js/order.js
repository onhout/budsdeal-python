import "../less/order.less";
// var Feedback = require('../../globals/Feedback/Feedback.js').default;
var BudsChat = require('./buds_chat').default;
var SellerProductList = require('./seller_products').default;
var Dialog = require('../../globals/Parts/Dialog').default;


$(function () {
    var chat_pane = $('#order_chats');

    function calculate_total() {
        var total = 0;
        $.each($('.order_subtotal'), function (i, v) {
            total += parseFloat($(v).text())
        });
        $('#order_total').text(total.toFixed(1));
    }

    if (chat_pane.length >= 1) {
        var chat = new BudsChat(chat_pane.data('chatid'), chat_pane.data('sender'));
    }

    $('[id$="item_amount"]').change(function () {
        var unit_price = parseFloat($(this).parents('tr').find('td > span.item_price').text());
        var value = parseFloat($(this).val());
        $(this).parents('tr').find('.order_subtotal').text(value * unit_price);
        calculate_total();
    });

    calculate_total();


    var finalize_btn = $('#finalize-order');
    finalize_btn.click(function (e) {
        e.preventDefault();
        $(this).attr('data-target', '#modal-' + $(this).data('id'));
        var modal = new Dialog({
            modal_title_text: 'Finalize',
            modal_body_text: 'Are you sure you want to finalize the order?',
            url: $(this).data('url'),
            id: $(this).data('id')
        });
        modal.run_modal();
    });
    finalize_btn.attr('data-toggle', 'modal');

    var shipping_btn = $('#shipping_btn');
    if (shipping_btn.length > 0) {
        $.get('/user/shipping/add/', function (data) {
            var modal = new Dialog({
                id: shipping_btn.data('id'),
                modal_body: $(data)
            });
            modal.run_modal();
        });
        shipping_btn.attr('data-target', '#modal-' + shipping_btn.data('id'));
        shipping_btn.attr('data-toggle', 'modal');
    }


    var add_product_btn = $('#add_product');
    if (add_product_btn.length > 0) {
        add_product_btn.click(function (e) {
            e.preventDefault();
            var table = new SellerProductList({
                order_id: $(this).data('order_id'),
                table_list: $('#order_list tbody')
            });
            var modal = new Dialog({
                modal_title_text: 'More products from seller',
                save_button: '<div/>',
                id: 'add_product',
                modal_body: table.table
            });
            modal.run_modal({
                size: 'lg'
            });
        });
        add_product_btn.attr('data-target', '#modal-add_product');
        add_product_btn.attr('data-toggle', 'modal')
    }

    var orderPicker = $('#datetimepicker');
    if (orderPicker.length > 0) {
        var date_storage = $('#id_order_form-expected_shipping_date').val();

        orderPicker.datetimepicker({
            format: 'MM/DD/YYYY',
        });

        orderPicker.data("DateTimePicker").date(new moment(date_storage));
    }


});