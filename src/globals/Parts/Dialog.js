class Dialog {
    constructor(data) {
        var self = this;
        this.id = data.id;
        this.url = data.url;
        this.save_button = data.save_button || $('<button/>', {
                'class': 'btn btn-primary btn-raised',
                'text': 'Submit'
            }).click(function () {
                    if (typeof self.url == 'string' && self.url) {
                        window.location.href = self.url;
                    } else {
                        if (self.validate_form(self.modal_body)) {
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
                        } else {
                            alert('Please fill out the required field')
                        }
                    }
                }
            );
        this.modal_body = data.modal_body || $('<p/>', {
                'text': data.modal_body_text
            });
        this.modal_title = data.modal_title || $('<h4/>', {
                'class': 'modal-title',
                'text': data.modal_title_text
            });

        this.close_button = $('<button/>', {
            'class': 'btn btn-default btn-raised',
            'data-dismiss': 'modal',
            'text': 'Close'
        });
    }

    run_modal(data) {
        var _data = data || {size: 'md'};
        var self = this;
        self.modal = $('<div/>', {
            'class': 'modal fade in',
            'data-backdrop': 'static',
            'id': 'modal-' + self.id
        })
            .append($('<div/>', {
                'class': 'modal-dialog modal-' + _data.size
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
                        .append(self.save_button))));
        self.modal.appendTo($('body'));
        self.modal.on('hidden.bs.modal', function (e) {
            self.modal.remove();
        });
    }

    validate_form(form) {
        var valid = true;
        form.find('.form-group input').each(function () {
            if ($(this).attr('required') && $(this).val() == '') {
                valid = false
            }
        });
        return valid;
    }
}

export default Dialog