// import { configureStore } from "@reduxjs/toolkit";
// import {composeWithDevTools} from 'redux-devtools-extension';
// import thunk from 'redux-thunk';
// import  rootReducer from './reducers';

import {configureStore} from '@reduxjs/toolkit'
import rootReducer from './reducers'


const store = configureStore({
    reducer: rootReducer,
    preloadedState: {}
})

export default store