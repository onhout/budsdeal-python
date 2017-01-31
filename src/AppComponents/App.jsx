import React from 'react';
import GlobalFooter from './GlobalFooter';
import GlobalNav from './GlobalNav';



class App extends React.Component {
    render() {
        const asas = require('../Bundles/Main').default;
        console.log(asas);
        return (
            <div>
                <GlobalNav/>
                <div className="container">
                    {this.props.children}
                </div>
                <GlobalFooter/>
            </div>
        );
    }
}

export default App;