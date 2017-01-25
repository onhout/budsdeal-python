import React, {Component} from 'react'

class MainPage extends Component {
    render() {
        const {info} = this.props;
        return (
            <div>
                <h2>Super Scalable Apps</h2>
                <p>
                    Open the network tab as you navigate. Notice that only the amount of
                    your app that is required is actually downloaded as you navigate
                    around. Even the route configuration objects are loaded on the fly.
                    This way, a new route added deep in your app will not affect the
                    initial bundle of your application..
                </p>
                <h2>Courses</h2>{info}
            </div>
        )
    }
}

export default MainPage