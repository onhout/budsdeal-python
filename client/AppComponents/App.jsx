import React from 'react';

import GlobalNav from './GlobalNav';
import Page from './Page';


class App extends React.Component {
    render() {
        return (
            <div>
                <GlobalNav/>
                <div className="container">
                    {this.props.children || <Page info={'dawd'}/>}
                </div>
            </div>
        );
    }
}

export default App;