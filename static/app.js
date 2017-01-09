/**
 * Created by pl on 1/7/17.
 */
requirejs.config({
	baseUrl: 'static/components',
	paths: {
		jquery: 'jquery/dist/jquery',
		bootstrap: 'bootstrap/dist/js/bootstrap',
		bundle: '../bundle'
	},
	shim:{
		bootstrap:{
			deps: ['jquery'],
			exports: 'Bootstrap'
		}
	}
});

require(['jquery','bootstrap', 'bundle'], function(){

});