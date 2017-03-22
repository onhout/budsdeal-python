var search_bar = require('./search_bar').default;

$(function () {
    $.material.init();
    var mainSearch = new search_bar();
    mainSearch.create('#Main_Search .typeahead', {
        index: '',
        searchParam: {
            count: 20,
            page: 1,
            category : 'Upgradeable',
            type: 'Sativa'
        }
    });
});