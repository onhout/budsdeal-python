class Dialog {
    constructor(title, text, url, id) {
        this.save_text = 'Yes';
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
            'text': this.save_text
        }).click(function () {
            window.location.href = url;
        });

        var modal = $('<div/>', {
            'class': 'modal fade in',
            'id': 'modal-' + id
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

export default Dialog