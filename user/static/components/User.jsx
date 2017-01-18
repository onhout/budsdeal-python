import React from 'react'
import '../less/user.less'

class User extends React.Component {

    render() {
        return (
            <div id="user">
                {this.props.children || <h1>Loading.....</h1>}
            </div>
        )
    }

}

export default User;