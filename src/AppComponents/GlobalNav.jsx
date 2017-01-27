import React, {Component} from 'react'
import {Link} from 'react-router'
import {Nav, Navbar, NavItem, NavDropdown, MenuItem} from 'react-bootstrap'
import {IndexLinkContainer, LinkContainer} from 'react-router-bootstrap'

class GlobalNav extends Component {

    constructor(props, context) {
        super(props, context)
        this.logOut = this.logOut.bind(this)
    }

    logOut() {
        alert('log out')
    }

    render() {
        const {user} = this.props;

        return (
            <Navbar inverse collapseOnSelect>
                <Navbar.Header>
                    <Navbar.Brand>
                        <a href="/">Budsdeal</a>
                    </Navbar.Brand>
                    <Navbar.Toggle />
                </Navbar.Header>
                <Navbar.Collapse>
                    <Nav>
                        <LinkContainer to="/main">
                            <NavItem eventKey={1}>Main</NavItem>
                        </LinkContainer>
                        <NavItem eventKey={2} href="#">Link</NavItem>
                        <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
                            <MenuItem eventKey={3.1}>Action</MenuItem>
                            <MenuItem eventKey={3.2}>Another action</MenuItem>
                            <MenuItem eventKey={3.3}>Something else here</MenuItem>
                            <MenuItem divider/>
                            <MenuItem eventKey={3.3}>Separated link</MenuItem>
                        </NavDropdown>
                    </Nav>
                    <Nav pullRight>
                        <LinkContainer to="/user/login">
                            <NavItem eventKey={2}>Login</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/user/signup">
                            <NavItem eventKey={2}>Signup</NavItem>
                        </LinkContainer>
                    </Nav>
                </Navbar.Collapse>
            </Navbar>
        )
    }
}

GlobalNav.defaultProps = {
    user: {
        id: 1,
        name: 'Ryan Florence'
    }
};

export default GlobalNav