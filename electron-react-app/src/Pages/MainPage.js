import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';

import Header from '../Components/Header'
import Fake_Data from "../Fake_Data.json"
import SideBar from '../Components/SideBar';
import MainInfo from '../Components/MainInfo';
import { PageContainer } from '../Resources/Themes/StyledComponents';
import { BodyContainer } from '../Resources/Themes/StyledComponents';


export default function MainPage() {
    const [data, setData] = useState({})
    const [clickedPerson, setClickedPerson] = useState([])
    let flightData = Fake_Data.Data



    const handlePersonOnClick = (flight, person) => {
        console.log(flight)
        console.log(person)
        setClickedPerson([flight, person])
        console.log(clickedPerson)
    };


    useEffect(() => {
        setData(flightData)
    }, [])

    return(
        <BodyContainer>
            <SideBar flightData={flightData} handlePersonOnClick={handlePersonOnClick}/>
            <MainInfo flightData={flightData} clickedPerson={clickedPerson}/>
        </BodyContainer>
    )
}