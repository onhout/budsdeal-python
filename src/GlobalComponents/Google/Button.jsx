import React from 'react'
import {Button} from 'react-bootstrap'

class GoogleButton extends React.Component {
    logIn(){
        alert('Log in or register')
    }

    render() {
        return (
            <div>
                <Button bsStyle="danger" onClick={this.logIn} bsSize="lg" block={true}>
                    <i className="fa fa-google-plus"></i> Google+ Login
                </Button>
            </div>
        )
    }

}

export default GoogleButton;