import React, {Component} from 'react';
import {Link, Navigate} from 'react-router-dom';
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {login} from '../../actions/auth';

import '../../stylesheets/LandingPage.css'

export class Login extends Component {
    state = {
        username: '',
        password: '',
    };

    static propTypes = {
        login: PropTypes.func.isRequired,
        isAuthenticated: PropTypes.bool,
    };

    onSubmit = (e) => {
        e.preventDefault();
        this.props.login(this.state.username, this.state.password);
    };

    onChange = (e) => this.setState({[e.target.name]: e.target.value});


    render() {
        if (this.props.isAuthenticated) {
            return <Navigate to="/list"/>;
        }
        const {username, password} = this.state;
        return (
            <div className="text-center m-5-auto">
                <h2>Sign in to us</h2>
                <form onSubmit={this.onSubmit}>
                    <div className="form-group">
                        <label>Username</label><br/>
                        <input
                            type="text"
                            className="form-control"
                            name="username"
                            onChange={this.onChange}
                            value={username}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label>Password</label>
                        <Link to="/forget-password"><label className="right-label">Forget password?</label></Link>
                        <br/>
                        <input
                            type="password"
                            className="form-control"
                            name="password"
                            onChange={this.onChange}
                            value={password}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <button id="sub_btn" type="submit">Login</button>
                    </div>
                </form>
                <footer>
                    <p>First time? <Link to="/register">Create an account</Link>.</p>
                    <p><Link to="/">Back to Homepage</Link>.</p>
                </footer>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, {login})(Login);
