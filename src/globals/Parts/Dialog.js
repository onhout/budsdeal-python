class Dialog {
    constructor(title, text, url, id) {
        var self = this;
        this.id = id;
        this.url = url;
        this.save_text = 'Yes';
        this.modal_body = $('<p/>', {
            'text': text
        });
        this.modal_title = $('<h4/>', {
            'class': 'modal-title',
            'text': title
        });

        this.close_button = $('<button/>', {
            'class': 'btn btn-default btn-raised',
            'data-dismiss': 'modal',
            'text': 'Close'
        });
    }

    run_modal() {
        var self = this;
        self.modal = $('<div/>', {
            'class': 'modal fade in',
            'id': 'modal-' + self.id
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
                        .append(self.modal_title))
                    .append($('<div/>', {
                        'class': 'modal-body'
                    })
                        .append(self.modal_body))
                    .append($('<div/>', {
                        'class': 'modal-footer'
                    })
                        .append(self.close_button)
                        .append($('<button/>', {
                            'class': 'btn btn-primary btn-raised',
                            'text': self.save_text
                        }).click(function () {
                            if (typeof self.url == 'string' && self.url) {
                                window.location.href = self.url;
                            } else {
                                $.ajax({
                                    type: "POST",
                                    url: self.modal_body.attr('action'),
                                    data: self.modal_body.serialize(),
                                    success: function (data) {
                                        if (data.status == 'success') {
                                            location.reload()
                                        } else {
                                            alert('An error occurred')
                                        }
                                    }
                                });
                            }
                        })))));
        self.modal.appendTo($('body'));
    }
}

export default Dialog