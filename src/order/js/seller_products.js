var csrf_token = require('../../globals/Utils/csrf_token').default;

class SellerProductList {
    constructor(data) {
        var self = this;
        this.table = $('<table/>', {
            class: "table table-hover table-bordered",
            id: 'add_user_product_table'
        })
            .append('<thead>' +
                '<tr>' +
                '<th>Item</th>' +
                '<th>Type</th>' +
                '<th>Price</th>' +
                '<th>Minimum Order</th>' +
                '<th>Select</th>' +
                '</tr>' +
                '</thead>');
        this.user_product_url = '/orders/list_seller_products/' + data.order_id + '?page=';
        this.order_id = data.order_id;
        this.currentPage = 1;
        this.prevBtn = $('<a/>', {
            class: "btn btn-success",
            text: "Prev",
        }).click(function (e) {
            if (!$(this).attr('disabled')) {
                self.get_page(self.currentPage - 1);
                self.currentPage -= 1;
            }
        });
        this.nextBtn = $('<a/>', {
            class: "btn btn-success",
            text: "Next"
        }).click(function (e) {
            if (!$(this).attr('disabled')) {
                self.get_page(self.currentPage + 1);
                self.currentPage += 1;
            }
        });
        this.table_list = data.table_list;
        this.paginate = $('<div/>', {
            class: 'pagination'
        }).append(this.prevBtn).append(this.nextBtn);

        this.get_page(this.currentPage);


    }

    get_page(page) {
        var self = this;
        $.get(self.user_product_url + page, function (data) {
            self.table.find('tbody').remove();
            var productCount = 0;
            var tbody = $('<tbody/>');
            $.each(data.data, function (i, v) {
                productCount += i;
                var tr = $('<tr/>');
                tbody.append(tr.append('<td class="text-center"><a href="/products/view/' + v.id + '" target="_blank"><img src="/' +
                    v.primary_photo + '" class="img-rounded" style="max-height: 56px"><p>' + v.name + '</p></a></td>' +
                    '<td>' + v.type + '</td>' +
                    '<td>$' + v.price + '</td>' +
                    '<td>' + v.min_count + ' ' + v.weight_unit + '</td>'));
                var product_select = $('<td>')
                    .append($('<a href="#" class="btn btn-primary">Select</a>').click(function () {
                        self.add_item(self.order_id, v, function (data) {
                            if (data.status == 'success') {
                                window.location.reload()
                            }
                        });
                        $('.modal').modal('hide');
                    }));
                tr.append(product_select)
            });
            self.currentPage <= 1 ? $(self.prevBtn.attr('disabled', true)) : $(self.prevBtn.attr('disabled', false));
            productCount < 5 ? $(self.nextBtn.attr('disabled', true)) : $(self.nextBtn.attr('disabled', false));
            self.table.append(tbody);
            self.table.after(self.paginate);
        })
    }

    add_item(order_id, item, callback) {
        $.post('/orders/item/add/' + order_id + '?item_id=' + item.id,
            {
                csrfmiddlewaretoken: '' + csrf_token.getCookie('csrftoken'),
                "order_items_form-item_amount": item.min_count
            },
            function (data) {
                callback(data)
            })
    }
}

export default SellerProductList