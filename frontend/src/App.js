import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import './App.css';

import PageNotFound from './components/pages/PageNotFound';
import LandingPage from './components/pages/LandingPage';
import LoginPage from './components/pages/Login';
import ListPage from './components/researcher/list';


import {Provider} from 'react-redux';
import store from './store';
import {loadUser} from './actions/auth'
import {Component} from "react";

class App extends Component {
    componentDidMount() {
        store.dispatch(loadUser());
    }

    render() {
        return (
            <Provider store={store}>
                <div className="App">
                    <Router>
                        {/*<Navbar/>*/}
                        <Routes>
                            <Route path='/' element={<LandingPage/>} exact/>
                            <Route path='/login' element={<LoginPage/>} exact/>
                            {/*<Route path='/signup' element={<Signup/>} exact/>*/}
                            {/*<Route path='/logout' element={<Logout/>} exact/>*/}
                            <Route path='/list' element={<ListPage/>} exact/>

                            <Route path='*' element={<PageNotFound/>} exact/>

                        </Routes>
                    </Router>
                </div>
            </Provider>
        );
    }
}

export default App;
