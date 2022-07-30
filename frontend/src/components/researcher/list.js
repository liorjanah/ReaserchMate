import React from 'react'

import '../../stylesheets/LandingPage.css'
import BackgroundImage from '../../static/images/bg.png'


export default function ListPage() {
    return (
        <header style={HeaderStyle}>
            <h1 className="main-title text-center">Testing page</h1>
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