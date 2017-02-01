class GoogleButton {

    static register (method) {
        var register = function(){
            alert(method+' clicked');
        };
        return $('<button/>', {
            class:'btn btn-social btn-google',
            text: method + ' with Google'
        }).append($('<span/>', {
            class: 'fa fa-google'
        })).click(register);
    }

    static login () {
        alert('Login Google!')
    }
}

export default GoogleButton;