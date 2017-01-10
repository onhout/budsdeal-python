// grab our gulp packages
var gulp  = require('gulp'),
    gutil = require('gulp-util'),
    gautoprefixer = require('gulp-autoprefixer'),
    gless = require('gulp-less'),
    gconcat = require('gulp-concat'),
    guglify = require('gulp-uglify');


// create a default task and just log a message
gulp.task('buildjs', function() {
  return gulp.src('**/static/js/*.js')
      .pipe(gconcat('bundle.js'))
      .pipe(guglify())
      .pipe(gulp.dest('static'))
});

gulp.task('buildcss', function(){
    var autoprefixerOptions = {
        browsers: ['last 2 versions']
    };
    var lessOptions = {
        paths: []
    };

    return gulp.src('**/static/less/*.less')
        .pipe(gless(lessOptions))
        .pipe(gautoprefixer(autoprefixerOptions))
        .pipe(gulp.dest('static'))
});

gulp.task('watch', function(){
    gulp.watch('**/static/js/*.js', []);
});

gulp.task('default', ['watch', 'buildjs', 'buildcss'], function(){
    return gutil.log('Done')
});