import React from 'react';
// import { Link } from 'react-router-dom';
import SearchBar from './searchBar';

const Navbar = () => {
    return (
        <nav className="rtl navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
            <a className="navbar-brand col-sm-3 col-md-2 mr-0" href="felagas.com">
                felagas
            </a>

            <SearchBar />
        </nav>
    );
};

export default Navbar;
