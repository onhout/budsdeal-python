/**
 * Created by pl on 1/7/17.
 */
requirejs.config({
	baseUrl: '/static/components',
	paths: {
		jquery: 'jquery/dist/jquery.min',
		bootstrap: 'bootstrap/dist/js/bootstrap.min',
		react: 'react/react-with-addons',
		reactdom:'react/react-dom.min',
		bundle: '../bundle'
	},
	shim:{
		bootstrap:{
			deps: ['jquery'],
			exports: 'Bootstrap'
		},
        reactdom:{
            deps: ['react'],
            exports: 'React'
        },
		bundle:{
			deps: ['react'],
            init: function(react){
                window.React = react;
            }
		}
	}
});

require(['jquery','bootstrap', 'react', 'reactdom', 'bundle'], function(jquery, bootstrap, react, reactdom, bundle){

});