var Dialog = require('./Dialog.js').default;

class BtnDelete {
    constructor() {
        var btn_delete = $('.btn-delete');
        btn_delete.click(function (e) {
            e.preventDefault();
            $(this).attr('data-target', '#modal-' + $(this).data('id'));
            var modal = new Dialog({
                modal_title_text: 'Delete',
                modal_body_text: 'Are you sure you want to delete?',
                url: $(this).data('url'),
                id: $(this).data('id')
            });

            modal.run_modal()
        });
        btn_delete.attr('data-toggle', 'modal');
    }
}

export default BtnDelete