var search_bar = require('./search_bar').default;

$(function () {
    $.material.init();
    var mainSearch = new search_bar();
    mainSearch.create('#Main_Search .typeahead');
    $(document).on('click', '.mega-dropdown', function (e) {
        e.stopPropagation();
    });

    //USER SIDEBAR

    $('#toggle-sidebar').click(function () {
        $('#cross').toggle();
        $('#bars').toggle();
        $('#wrapper').toggleClass('toggled');
    });
});