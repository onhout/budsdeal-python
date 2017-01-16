import React from 'react';
// import AwesomeComponent from '../../user/static/js/user';
// import MainComponent from './js/main';
import Nav from './AppComponents/Nav';

class Main extends React.Component {
    render() {
        return (
            <div>
                <Nav/>
                <p> Hello React!</p>
                {this.props.children}
            </div>
        );
    }
}

export default Main;