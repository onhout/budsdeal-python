import "../less/user.less";
// const fbButton = $('#facebookButton');
// const googButton = $('#googleButton');
// var FB = require('../../globals/Facebook/Button').default;
// var GOOGLE = require('../../globals/Google/Button').default;
// fbButton.append(FB.register(fbButton.data('method')));
// googButton.append(GOOGLE.register(googButton.data('method')));

$(function () {
    $('#toggle-sidebar').click(function () {
        $('#cross').toggle();
        $('#bars').toggle();
        $('#wrapper').toggleClass('toggled');
    })
});