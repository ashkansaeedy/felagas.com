import React from 'react';

const Footer = () => {
    return (
        <footer className="rtl float-left fixed-bottom navbar navbar-dark bg-dark col-md-9 ml-sm-auto col-lg-10 px-4 shadow">
            <div className="copyright">
                <span className="fa fa-copyright m-1" />
                By ashkan saeedy 
                </div>
                <div className="socialmedia">
                <a href="https://www.instagram.com/_felagas_/"
                    className="fa fa-instagram m-1"/>
                {/* <a
                    className="fa fa-facebook-official m-1"
                    href=''
                /> */}
            </div>
        </footer>
    );
};

export default Footer;
