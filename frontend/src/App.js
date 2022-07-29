// import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import PageNotFound from './components/pages/PageNotFound'
import LandingPage from './components/pages/LandingPage';

import './App.css';


function App() {
    return (
        <div className="App">
            <Router>
                {/*<Navbar/>*/}
                <Routes>
                    <Route path='/' element={<LandingPage/>} exact/>

                    {/*<Route path='/login' element={<Login/>} exact/>*/}
                    {/*<Route path='/signup' element={<Signup/>} exact/>*/}
                    {/*<Route path='/logout' element={<Logout/>} exact/>*/}
                    <Route path='*' element={<PageNotFound/>} exact/>

                </Routes>
            </Router>
        </div>
    );
}

export default App;
