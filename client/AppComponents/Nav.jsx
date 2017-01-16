import React from "react";

class Nav extends React.Component {
    constructor(props, context) {
        super(props, context)
    }

    render() {
        return (
            <nav className="navbar navbar-default">
                <div className="container-fluid">
                    <div className="navbar-header">
                        <button type="button" className="navbar-toggle collapsed">
                            <span className="sr-only">Toggle navigation</span>
                            <span className="icon-bar"></span>
                            <span className="icon-bar"></span>
                            <span className="icon-bar"></span>
                        </button>
                        <a className="navbar-brand" href="/">Budsdeal</a>
                    </div>
                    <div className="collapse navbar-collapse" id="menu-collapse">
                        <ul className="nav navbar-nav">
                            <li><a href="/asd/">About</a></li>
                        </ul>
                        <ul className="nav navbar-nav navbar-right">
                            <li><a href="{% url 'user_login' %}">Login</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        )
    }
}

export default Nav;