class SearchBar {
    constructor() {
        this.searchDatum = function (target_index, searchParam) {
            target_index = target_index ? target_index : '';
            var param = searchParam ? searchParam : {"count": 11, 'page': 1};
            param.count += 1;
            return new Bloodhound({
                datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
                queryTokenizer: Bloodhound.tokenizers.whitespace,
                // prefetch: '/autocomplete/?search=&count=11&page=1',
                remote: {
                    url: '/autocomplete/' + target_index + '?search=%QUERY&' + $.param(param),
                    //TODO maybe make a search param for target_index in the future
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
            templates: {
                suggestion: this.template
            }
        }
    }

    create(ele, target) {
        var index = {};
        if (target) {
            this.dataset.limit = target.searchParam ? target.searchParam.count : '10';
            index = {
                name: target.index,
                source: this.searchDatum(target.index, target.searchParam)
            }
        }
        else {
            this.dataset.limit = '10';
            index = {
                name: 'products',
                source: this.searchDatum()
            };
        }

        $.extend(this.dataset, index);

        $(ele).typeahead(this.options, this.dataset);
        $(ele).bind('typeahead:select', function (ev, suggestion) {
            $(this).typeahead("val", "");
            location.href = '/products/view/' + suggestion.product_id;
        });
    }
}

export default SearchBar;