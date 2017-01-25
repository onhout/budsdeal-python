import React, {Component} from 'react'
import {Link} from 'react-router'
import {IndexLinkContainer, LinkContainer} from 'react-router-bootstrap'

var style = {
    backgroundColor: "#F8F8F8",
    borderTop: "1px solid #E7E7E7",
    textAlign: "center",
    padding: "20px",
    position: "fixed",
    left: "0",
    bottom: "0",
    height: "60px",
    width: "100%",
};

var phantom = {
    display: 'block',
    padding: '20px',
    height: '60px',
    width: '100%',
};

var footerColor = {
    color: 'gray'
};


class GlobalFooter extends Component {
    render() {
        return (
            <div>
                <div style={phantom}>
                    <div style={style}>
                        <p className="text-muted">Copyrighted @Budsdeal 2017</p>
                    </div>
                </div>
            </div>
        )
    }
}

export default GlobalFooter;