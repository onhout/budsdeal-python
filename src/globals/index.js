var search_bar = require('./search_bar').default;
var delete_modal = require('./Parts/Delete').default;

$(function () {
    $.material.init();
    var mainSearch = new search_bar();
    mainSearch.create('#Main_Search .typeahead');
    new delete_modal();
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