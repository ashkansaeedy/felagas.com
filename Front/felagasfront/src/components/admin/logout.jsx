import { Component } from 'react';
// import React from 'react';

class Logout extends Component {
    componentDidMount() {
        localStorage.removeItem('token');
        window.location = '/';
    }

    render() {
        return null;
    }
}

export default Logout;
