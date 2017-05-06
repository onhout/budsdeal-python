var Dialog = require('./Dialog.js').default;

class BtnCancel {
    constructor() {
        var btn_cancel = $('.btn-cancel');
        btn_cancel.click(function (e) {
            e.preventDefault();
            $(this).attr('data-target', '#modal-' + $(this).data('id'));
            var modal = new Dialog({
                modal_title_text: 'Cancel',
                modal_body_text: 'Are you sure you want to cancel?',
                url: $(this).data('url'),
                id: $(this).data('id')
            });
            modal.run_modal()
        });
        btn_cancel.attr('data-toggle', 'modal');
    }
}

export default BtnCancel