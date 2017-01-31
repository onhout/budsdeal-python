import React from 'react';
import GlobalFooter from './GlobalFooter';
import GlobalNav from './GlobalNav';


class App extends React.Component {
    render() {
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