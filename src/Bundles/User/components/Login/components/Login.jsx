import React from 'react'
import FacebookButton from '../../Facebook/Button'
import GoogleButton from '../../Google/Button'
import {Form, FormGroup, ControlLabel, FormControl, HelpBlock, Button, Col} from 'react-bootstrap'
import DjangoCSRFToken from '../../../../../../src/Utils/CSRFToken'


class Login extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: ''
        };
        this.handleValidation = this.handleValidation.bind(this);
        //React components using ES6 classes no longer autobind this to non React methods
        //http://www.newmediacampaigns.com/blog/refactoring-react-components-to-es6-classes
    }

    getValidationState(input) {
        // regex from http://stackoverflow.com/questions/46155/validate-email-address-in-javascript
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        const bool = re.test(input);
        if (bool) return 'success';
        else return 'error';
    }

    handleValidation(e) {
        this.setState({
            email: e.target.value
        });
    }

    render() {
        return (
            <Col xs={12} md={8} mdOffset={2}>
                <Form>
                    <FormGroup
                        controlId="email"
                        validationState={this.getValidationState(this.state.email)}
                        bsSize="lg"
                    >
                        <ControlLabel>Username</ControlLabel>
                        <FormControl
                            type="email"
                            value={this.state.email}
                            placeholder="Enter email"
                            onChange={this.handleValidation}
                        />
                        <FormControl.Feedback />
                        <HelpBlock>Enter your email address</HelpBlock>
                    </FormGroup>
                    <FormGroup
                        controlId="password"
                        bsSize="lg"
                    >
                        <ControlLabel>Password</ControlLabel>
                        <FormControl
                            type="password"
                            value={this.state.password}
                            placeholder="Enter password"
                        />
                        <FormControl.Feedback />
                    </FormGroup>
                    <DjangoCSRFToken/>
                    <FormGroup className="pull-right">
                        <Button type="submit" bsSize="lg">
                            Sign in
                        </Button>
                    </FormGroup>

                    <FacebookButton/>
                    <div style={{marginTop: 10}}>
                        <GoogleButton/>
                    </div>
                </Form>
            </Col>
        );
    }

}

export default Login;