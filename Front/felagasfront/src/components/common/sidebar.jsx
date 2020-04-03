import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { getCourseCount } from '../../services/courseService';
import getNavLinks from '../../services/navLinks';
import UserInfo from './userInfo';

class Sidebar extends Component {
    state = {
        courseCount: ''
    };
    async componentDidMount() {
        const { data: courseCount } = await getCourseCount();
        console.log(courseCount);
        this.setState({ courseCount: courseCount.count });
    }
    render() {
        const navLinks = getNavLinks();
        return (
            <nav className="col-md-2 d-none d-md-block bg-light sidebar">
                <div className="sidebar-sticky">
                    <UserInfo
                        imgUrl="http://www.imgurl.ir/uploads/s245306_Screenshot_from_2018-10-26_074736.png"
                        fullname="یونس قربانی"
                        text="برنامه نویس و مهندس امنیت"
                    />
                    <hr className="shadow" />

                    <ul className="nav flex-column">
                        {navLinks.map(nav => (
                            <li className="nav-item" key={nav.id}>
                                <Link className="nav-link" to={nav.link}>
                                    <span className={nav.icon} />
                                    <span className="m-2">{nav.text}</span>
                                    {nav.text === 'دوره ها' ? (
                                        <span className="badge-danger badge-pill">
                                            {this.state.courseCount}
                                        </span>
                                    ) : null}
                                </Link>
                            </li>
                        ))}
                    </ul>
                </div>
            </nav>
        );
    }
}

export default Sidebar;
