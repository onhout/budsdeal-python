/**
 * Created by pl on 1/7/17.
 */
requirejs.config({
	baseUrl: '/static/components',
	paths: {
		jquery: 'jquery/dist/jquery.min',
		bootstrap: 'bootstrap/dist/js/bootstrap.min',
		bundle: '../bundle'
	},
	shim:{
		bootstrap:{
			deps: ['jquery'],
			exports: 'Bootstrap'
		},
		bundle:{
			deps: ['jquery']
		}
	}
});

require(['jquery','bootstrap', 'bundle'], function(){

});