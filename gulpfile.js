// grab our gulp packages
var gulp = require('gulp'),
    gutil = require('gulp-util'),
    gwebpack = require('webpack-stream'),
    gautoprefixer = require('gulp-autoprefixer'),
    gless = require('gulp-less'),
    gminifycss = require('gulp-minify-css'),
    gconcat = require('gulp-concat'),
    gdel = require('del'),
    gplumber = require('gulp-plumber'),
    gbabel = require('gulp-babel'),
    guglify = require('gulp-uglify');

var errorHandler = function(){
    // default appearance
    return gplumber(function(error){
        // output styling
        gutil.log('|- ' + gutil.colors.bgRed.bold('Build Error in ' + error.plugin));
        gutil.log('|- ' + gutil.colors.bgRed.bold(error.message));
    });
};

// create a default task and just log a message
// gulp.task('buildjs', function() {
//   return gulp.src('**/static/js/*.js')
//       .pipe(gbabel({
//           presets:['es2015']
//       }))
//       .pipe(gconcat('bundle.js'))
//       .pipe(guglify())
//       .pipe(gulp.dest('static'))
// });
gulp.task('clean-dist', function () {
    return gdel([
        './static/*'
    ])
});
gulp.task('webpack', function () {
    return gulp.src('/client/index.js')
        .pipe(errorHandler())
        .pipe(gwebpack(require('./webpack.config.js')))
        .pipe(gulp.dest('./static/'));
});

// gulp.task('buildcss', function () {
//     var autoprefixerOptions = {
//         browsers: ['last 2 versions']
//     };
//     var lessOptions = {
//         paths: []
//     };
//
//     return gulp.src('**/static/less/*.less')
//         .pipe(errorHandler())
//         .pipe(gless(lessOptions))
//         .pipe(gconcat('styles.css'))
//         .pipe(gminifycss())
//         .pipe(gautoprefixer(autoprefixerOptions))
//         .pipe(gulp.dest('/static/'))
// });

gulp.task('watch', function () {
    gulp.watch(['**/static/index.js', 'client/**', '**/static/js/*.jsx'], ['clean-dist', 'webpack']);
});

gulp.task('default', ['clean-dist', 'webpack', 'watch'], function () {
    return gutil.log('Done')
});