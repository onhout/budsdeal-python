class Delete {
    constructor() {
        var self = this;
        var btn_delete = $('.btn-delete');
        btn_delete.click(function (e) {
            e.preventDefault();
            $(this).attr('data-target', '#delete-modal-' + $(this).data('id'));
            self.create_overlay('Delete',
                'Are you sure you want to delete?',
                $(this).data('url'),
                $(this).data('id'));
            // $('#delete-modal').modal(options)
        });
        btn_delete.attr('data-toggle', 'modal');


    }

    create_overlay(title, text, url, id) {
        var modal_title = $('<h4/>', {
            'class': 'modal-title',
            'text': title
        });
        var modal_body = $('<p/>', {
            'text': text
        });
        var close_button = $('<button/>', {
            'class': 'btn btn-default btn-raised',
            'data-dismiss': 'modal',
            'text': 'Close'
        });

        var accept_button = $('<button/>', {
            'class': 'btn btn-primary btn-raised',
            'text': 'Save Changes'
        }).click(function () {
            window.location.href = url;
        });

        var modal = $('<div/>', {
            'class': 'modal fade in',
            'id': 'delete-modal-' + id
        })
            .append($('<div/>', {
                'class': 'modal-dialog'
            })
                .append($('<div/>', {
                    'class': 'modal-content'
                })
                    .append($('<div/>', {
                        'class': 'modal-header'
                    })
                        .append($('<button/>', {
                            'type': 'button',
                            'class': 'close',
                            'data-dismiss': 'modal',
                            'aria-hidden': 'true',
                            'text': 'x'
                        }))
                        .append(modal_title))
                    .append($('<div/>', {
                        'class': 'modal-body'
                    })
                        .append(modal_body))
                    .append($('<div/>', {
                        'class': 'modal-footer'
                    })
                        .append(close_button)
                        .append(accept_button))));
        modal.appendTo($('body'));
    }
}

export default Delete