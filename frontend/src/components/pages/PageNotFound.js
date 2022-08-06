import React from 'react'
import {Link} from 'react-router-dom'

import BackgroundImage from '../../static/images/page_not_found.jpeg'


export default function LandingPage() {
    return (
        <header style={HeaderStyle}>
            <div className="buttons text-center">
                <Link to="/">
                    <button className="primary-button" style={BackButtonStyle}>I'll go to the home page</button>
                </Link>
            </div>
        </header>
    )
}

const HeaderStyle = {
    width: "100%",
    height: "100vh",
    background: `url(${BackgroundImage})`,
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    backgroundSize: "cover"
}

const BackButtonStyle = {
    width: "fit-content"
}