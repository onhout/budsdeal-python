var search_bar = require('./search_bar').default;
var delete_button = require('./Parts/btn-delete').default;
var cancel_button = require('./Parts/btn-cancel').default;


$(function () {
    $.material.init();
    var mainSearch = new search_bar();
    mainSearch.create('#Main_Search .typeahead');
    new delete_button();
    new cancel_button();
    $(document).on('click', '.mega-dropdown', function (e) {
        e.stopPropagation();
    });

    //USER SIDEBAR

    $('#toggle-sidebar').click(function () {
        $('#cross').toggle();
        $('#bars').toggle();
        $('#wrapper').toggleClass('toggled');
        $('#wrapper-order').toggleClass('toggled');
    });
});