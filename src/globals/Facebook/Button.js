class FacebookButton {

    static register (method) {
        var register = function(){
            alert(method+' clicked');
        };
        return $('<button/>', {
            class:'btn btn-social btn-facebook',
            text: method + ' with Facebook'
        }).append($('<span/>', {
            class: 'fa fa-facebook'
        })).click(register);
    }

    static login () {
        alert('Login Facebook!')
    }
}

export default FacebookButton;