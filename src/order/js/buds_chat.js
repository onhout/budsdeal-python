class BudsChat {
    constructor(id, sender) {
        var self = this;
        this.sender = sender;
        this.socket = new WebSocket("ws://" + window.location.host + "/chat?order_id=" + id);
        this.socket.onmessage = function (e) {
            var message = JSON.parse(e.data);
            message.timestamp = moment().format('M/D/YY h:mmA');
            self.chatPane.append(self.chat_module(message));

            self.chatBody.animate({
                scrollTop: self.chatPane.prop('scrollHeight')
            }, 500)
        };
        this.chatBody = $('#order_chats .panel-body');
        this.chatPane = $('ul.chat');
        this.inputField = $('#order_message');
        this.sendButton = $('#send_order_message');
        this.inputField.on('keydown', function (e) {
            if (e.which == 13) {
                e.preventDefault();
                self.send_message();
                self.reset_field();
            }
        });


        this.sendButton.on('click', function () {
            self.send_message();
            self.reset_field();
        });

        if (this.socket.readyState == WebSocket.OPEN) this.socket.onopen();
        self.chatBody.animate({
            scrollTop: self.chatPane.prop('scrollHeight')
        }, 500)
    }

    reset_field() {
        this.inputField.val('')
    };

    send_message() {
        if (this.inputField.val()) {
            this.socket.send(this.inputField.val())
        }
    };

    chat_module(data) {
        var chat_position = this.sender == data.display_name ? 'right' : 'left';
        var chat_right = this.sender == data.display_name ? 'pull-right' : '';
        var chat_left = this.sender == data.display_name ? '' : 'pull-right';
        var wrap = $('<li/>', {
            'class': chat_position + ' clearfix'
        });

        var profile_photo = $('<span/>', {
            'class': 'chat-img pull-' + chat_position
        }).append($('<img/>', {
            'src': data.profile_pic,
            'class': 'img-circle',
            'style': 'width: 50px'
        }));

        var chatBody = $('<div>', {
            'class': 'chat-body clearfix'
        })
            .append($('<div>', {
                'class': 'header'
            })
                .append($('<strong class=' + chat_right + '>' + data.full_name + '</strong>'))
                .append($('<small/>', {
                        'class': chat_left + ' text-muted'
                    })
                        .append($('<span/>', {
                            'class': 'glyphicon glyphicon-time'
                        }))
                        .append(data.timestamp)
                ))
            .append($('<p>' + data.msg + '</p>'));

        return wrap
            .append(profile_photo)
            .append(chatBody)

    }
}

export default BudsChat