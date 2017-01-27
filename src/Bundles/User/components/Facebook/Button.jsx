import React from 'react'
import {Button} from 'react-bootstrap'

class FacebookButton extends React.Component {
    logIn(){
        alert('Log in or register')
    }

    render() {
        return (
            <div>
                <Button bsStyle="primary" onClick={this.logIn} bsSize="lg" block={true}>
                    <i className="fa fa-facebook-official"></i> Facebook Login
                </Button>
            </div>
        )
    }

}

export default FacebookButton;