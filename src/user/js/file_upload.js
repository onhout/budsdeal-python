var csrf_token = require('../../globals/Utils/csrf_token').default;

class ImageUpload {
    constructor(element) {
        var id_image = $(element);
        id_image.click();

        id_image.fileupload({
            dataType: 'json',
            sequentialUploads: true,
            acceptFileTypes: /(\.|\/)(jpe?g|png)$/i,
            start: function (e) {  /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
                $('.progress').show();
            },
            stop: function (e) {  /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
                $('.progress').hide();
            },
            progressall: function (e, data) {  /* 4. UPDATE THE PROGRESS BAR */
                var progress = parseInt(data.loaded / data.total * 100, 10);
                var strProgress = progress + "%";
                $(".progress-bar").css({"width": strProgress});
                // $(".progress-percentage").text(strProgress);
            },
            done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
                if (data.result.is_valid) {
                    var imageTableRow = new ImageTableRow(data, csrf_token);
                    $('#product_gallery tbody').prepend(imageTableRow);
                }
            }
        })
    }

    static deleteFN(image_id, csrftoken, SELF) {
        return function (e) {
            e.preventDefault();
            var self = this || SELF;
            var href = '/products/image/delete/' + image_id + '/';
            $.post(href, csrftoken, function (data) {
                if (data.success) {
                    $(self).closest('tr').remove();
                }
            })
        }
    }
}

class ImageTableRow {

    constructor(data, csrfToken) {
        var self = this;
        this.row = $('<tr>');
        this.imgLink = $('<a>', {
            href: data.result.url
        });
        this.img = $('<img>',
            {
                'class': 'img-responsive img-rounded',
                'src': data.result.url,
                'style': 'max-height:56px'
            });
        this.updated = $('<td>' + data.result.updated_at + '</td>');
        this.deleteBtn = $('<a/>',
            {
                'class': 'btn btn-danger btn-raised delete_photo',
                'text': 'Delete'
            }).click(ImageUpload.deleteFN(data.result.image_id,
            {csrfmiddlewaretoken: '' + csrfToken.getCookie('csrftoken')}));

        this._row = this.row
            .append($('<td>').append(this.imgLink.append(this.img)))
            .append(this.updated)
            .append($('<td>').append(this.deleteBtn));

        return this._row;
    }
}

export default ImageUpload