class SellerProductList {
    constructor(data) {
        this.table = $('<table/>', {
            class: "table table-hover table-bordered",
            id: 'add_user_product_table'
        })
            .append('<thead>' +
                '<tr>' +
                '<th>Item</th>' +
                '<th>Type</th>' +
                '<th>Price</th>' +
                '<th>Category</th>' +
                '</tr>' +
                '</thead>')
            .append('<tbody/>');
        this.page = 1;
        this.user_product_url = '/orders/list_seller_products/' + data.order_id + '?page=' + this.page;
        $.get(this.user_product_url, function (data) {
            $.each(data.data, function (i, v) {
                this.table.find('<tbody>').append('<tr>' +
                    '<td>' + v.name + '</td>' +
                    '<td>' + v.type + '</td>' +
                    '<td>' + v.price + '</td>' +
                    '<td>' + v.categories + '</td>' +
                    '</tr>')
            })
        })
    }
}

export default SellerProductList