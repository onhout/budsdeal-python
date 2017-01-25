import React from 'react';
import GlobalFooter from './GlobalFooter';
import GlobalNav from './GlobalNav';
import MainPage from './MainPage';


class App extends React.Component {
    render() {
        return (
            <div>
                <GlobalNav/>
                <div className="container">
                    {this.props.children || <MainPage info={'dawd'}/>}
                </div>
                <GlobalFooter/>
            </div>
        );
    }
}

export default App;