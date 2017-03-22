class SearchBar {
    constructor() {
        this.searchDatum = function (target_index, searchParam) {
            target_index = target_index ? target_index : '';
            var param = searchParam ? searchParam : {"count": 11, 'page': 1};
            return new Bloodhound({
                datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
                queryTokenizer: Bloodhound.tokenizers.whitespace,
                // prefetch: '/autocomplete/?search=&count=11&page=1',
                remote: {
                    url: '/autocomplete/' + target_index + '?search=%QUERY&' + $.param(param),
                    wildcard: '%QUERY'
                }
            });
        };

        this.template = function (e) {
            return '<li class="list-group-item text-nowrap">' + e.name + ' – '
                + e.brand + '</li>'
        };
        this.options = {
            hint: true,
            highlight: true,
            minLength: 1
        };
        this.dataset = {
            limit: 10,
            templates: {
                suggestion: this.template
            }
        }
    }

    create(ele, target_index) {
        var index = target_index ? {
            name: target_index,
            source: this.searchDatum(target_index, searchParam)
        } : {
            name: 'products',
            source: this.searchDatum()
        };
        $.extend(this.dataset, index);

        $(ele).typeahead(this.options, this.dataset)
    }
}

// var products = new Bloodhound({
//     datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
//     queryTokenizer: Bloodhound.tokenizers.whitespace,
//     // prefetch: '/autocomplete/?search=&count=11&page=1',
//     remote: {
//         url: '/autocomplete/?search=%QUERY&count=11&page=1',
//         wildcard: '%QUERY'
//     }
// });
//
// $('#Main_Search .typeahead').typeahead({
//     hint: true,
//     highlight: true,
//     minLength: 1
// }, {
//     name: 'products',
//     source: products,
//     limit: 10,
//     templates: {
//         suggestion: function (e) {
//             return '<li class="list-group-item text-nowrap">' + e.name + ' – '
//                 + e.brand + '</li>'
//         }
//     }
// });

$('.typeahead').bind('typeahead:select', function (ev, suggestion) {
    $(this).typeahead("val", "");
    location.href = '/products/view/' + suggestion.product_id;
});

export default SearchBar