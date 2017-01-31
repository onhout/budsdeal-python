import React from "react";
import {render} from "react-dom";
// import {Provider} from "react-redux";
import {Router, Route, IndexRoute, hashHistory} from "react-router";
import 'jquery';
import 'bootstrap/dist/js/bootstrap';
import './Less/App.less';

const rootRoute = {
    path: '/',
    component: require('./AppComponents/App').default,
    indexRoute:require ('./AppComponents/MainPage').default,
    childRoutes: [
        require('./Bundles/Main').default,
        require('./Bundles/User').default
        // require('./routes/Course')
    ]
};


render((
    <Router history={hashHistory} routes={rootRoute}/>
), document.getElementById('react-app'));
