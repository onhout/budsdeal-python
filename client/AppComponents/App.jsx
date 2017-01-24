import React from 'react';
import GlobalFooter from './GlobalFooter';
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
                <GlobalFooter/>
            </div>
        );
    }
}

export default App;