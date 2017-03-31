class Feedback {
    constructor(submit) {
        var _this = this;
        this.star = $('.buds_star').addClass('fa-2x');
        // this.feedbackURL = '/' + target + '/feedback/' + this.star.data('feedback_' + target);
        this.numStars = 5;
        this.rating = Math.round(this.star.data('feedback_rating')) || 0;
        this.change = function (e, value) {
        };
        this.createStars();
        this.syncRating();
        this.star.tooltip({
            trigger: 'hover focus',
            placement: 'bottom',
            title: this.star.data('feedback_rating_count') ? 'Based on ' + this.star.data('feedback_rating_count') +
            ' rating(s)' : 'No ratings yet!'
        });
        if (submit == true) {
            this.star.on('mouseover.buds_star', 'i', function (e) {
                return _this.syncRating(_this.star.find('i').index(e.currentTarget) + 1);
            });
            this.star.on('mouseout.buds_star', function () {
                return _this.syncRating();
            });
            this.star.on('click.buds_star', 'i', function (e) {
                return _this.setRating(_this.star.find('i').index(e.currentTarget) + 1);
            });
            this.star.on('buds_star:change', this.change);
        }

    }

    setRating(rating) {
        if (this.rating === rating) {
            rating = void 0;
        }
        this.rating = rating;
        this.syncRating();
        return this.star.trigger('buds_star:change', rating);
    }

    createStars() {
        var _i, _ref, _results;

        _results = [];
        for (_i = 1, _ref = this.numStars; 1 <= _ref ? _i <= _ref : _i >= _ref; 1 <= _ref ? _i++ : _i--) {
            _results.push(this.star.append("<i class='fa fa-star-o'></i>"));
        }
        return _results;
    }

    syncRating(rating) {
        var i, _i, _j, _ref;

        rating || (rating = this.rating);
        if (rating) {
            for (i = _i = 0, _ref = rating - 1; 0 <= _ref ? _i <= _ref : _i >= _ref; i = 0 <= _ref ? ++_i : --_i) {
                this.star.find('i').eq(i).removeClass('fa-star-o').addClass('fa-star text-warning');
            }
        }
        if (rating && rating < 5) {
            for (i = _j = rating; rating <= 4 ? _j <= 4 : _j >= 4; i = rating <= 4 ? ++_j : --_j) {
                this.star.find('i').eq(i).removeClass('fa-star text-warning').addClass('fa-star-o');
            }
        }
        if (!rating) {
            return this.star.find('i').removeClass('fa-star text-warning').addClass('fa-star-o');
        }
    }

    _post() {

    }
}

export default Feedback