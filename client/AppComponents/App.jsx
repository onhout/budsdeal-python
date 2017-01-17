import React from 'react';
// import AwesomeComponent from '../../user/static/js/user';
// import MainComponent from './js/main';
import Nav from './Nav';
import Page from './Page';

class App extends React.Component {
    render() {
        return (
            <div>
                <Nav/>
                <p> Hello React!</p>
                <Page courses={'dawd'}/>
                <div>
                    {this.props.children || <h1>Free</h1>}
                </div>
            </div>
        );
    }
}

export default App;