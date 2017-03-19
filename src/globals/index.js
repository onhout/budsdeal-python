$(function () {
    $.material.init();

    var products = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        prefetch: '/autocomplete/?search=&count=11&page=1',
        remote: {
            url: '/autocomplete/?search=%QUERY&count=20&page=1',
            wildcard: '%QUERY'
        }
    });

    $('#Main_Search .typeahead').typeahead({
        hint: true,
        highlight: true,
        minLength: 1
    }, {
        name: 'products',
        source: products,
        limit: 10,
        templates: {
            suggestion: function (e) {
                return '<li class="list-group-item text-nowrap">' + e.name + ' – '
                    + e.brand + '</li>'
            }
        }
    });

    $('.typeahead').bind('typeahead:select', function (ev, suggestion) {
        $(this).typeahead("val", "");
        location.href = '/products/view/' + suggestion.product_id;
    });

});