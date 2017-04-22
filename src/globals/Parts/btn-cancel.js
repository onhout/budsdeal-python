var Dialog = require('./Dialog.js').default;

class BtnCancel {
    constructor() {
        var btn_cancel = $('.btn-cancel');
        btn_cancel.click(function (e) {
            e.preventDefault();
            $(this).attr('data-target', '#modal-' + $(this).data('id'));
            var modal = new Dialog('Cancel',
                'Are you sure you want to cancel?',
                $(this).data('url'),
                $(this).data('id'));
            modal.run_modal()
        });
        btn_cancel.attr('data-toggle', 'modal');
    }
}

export default BtnCancel