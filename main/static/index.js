import React from 'react';
import AwesomeComponent from '../../user/static/js/user';
import MainComponent from './js/main';

class Main extends React.Component {
    render() {
        return (
            <div>
                <p> Hello React!</p>
                <MainComponent/>
                <AwesomeComponent />
            </div>
        );
    }
}

export default Main;