import React from "react";
import {render} from "react-dom";
import {Provider} from "react-redux";
import {Router, browserHistory} from "react-router";

const rootRoute = {
    childRoutes: [{
        path: '/',
        component: require('./App'),
        childRoutes: [
            // require('./routes/Calendar'),
            // require('./routes/Course')
        ]
    }]
};


render(<Router
    history={browserHistory}
    routes={rootRoute}
/>, document.getElementById('react-app'));
