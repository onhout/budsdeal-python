/**
 * Created by pl on 1/7/17.
 */
requirejs.config({
	baseUrl: 'static/components',
	paths: {
		jquery: 'jquery/dist/jquery',
		bootstrap: 'bootstrap/dist/js/bootstrap'
	},
	shim:{
		bootstrap:{
			deps: ['jquery'],
			exports: 'Bootstrap'
		}
	}
});

require(['jquery','bootstrap'], function(){
    console.log('there');
});