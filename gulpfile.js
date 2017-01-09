// grab our gulp packages
var gulp  = require('gulp'),
    gutil = require('gulp-util'),
    gconcat = require('gulp-concat'),
    guglify = require('gulp-uglify');


// create a default task and just log a message
gulp.task('buildjs', function() {
  return gulp.src('**/static/js/*.js')
      .pipe(gconcat('bundle.js'))
      .pipe(guglify())
      .pipe(gulp.dest('static'))
});

gulp.task('watch', function(){
    gulp.watch('**/static/js/*.js', []);
});

gulp.task('default', ['watch', 'buildjs'], function(){
    return gutil.log('Done')
});