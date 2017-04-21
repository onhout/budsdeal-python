var Dialog = require('./Dialog.js').default;

class BtnDelete {
    constructor() {
        var btn_delete = $('.btn-delete');
        btn_delete.click(function (e) {
            e.preventDefault();
            $(this).attr('data-target', '#modal-' + $(this).data('id'));
            new Dialog('Delete',
                'Are you sure you want to delete?',
                $(this).data('url'),
                $(this).data('id'));
        });
        btn_delete.attr('data-toggle', 'modal');
    }
}

export default BtnDelete