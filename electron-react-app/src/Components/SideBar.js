import React, { useState, useEffect } from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionDetails from '@mui/material/AccordionDetails';
import AccordionSummary from '@mui/material/AccordionSummary';
import { SideBarContainer } from '../Resources/Themes/StyledComponents';
import Collapsible from 'react-collapsible'


export default function SideBar({flightData, handlePersonOnClick}) {

    return(
        <SideBarContainer>
            72nd Sections
            <ul>
                {Object.keys(flightData).map((flight, i) => (
                    <li key={i}>
                    <Collapsible trigger={flight}>
                        <ul>
                            {Object.keys(flightData[flight]).map((person, j) => (
                                <li key={j} onClick={() => handlePersonOnClick(flight, person)}>{person}</li>
                            ))}
                        </ul>
                    </Collapsible>
                    </li>
                ))}
            </ul>
        </SideBarContainer>
    )
}

    //const [clickedPerson, setClickedPerson] = useState()


    // const handlePersonOnClick = (e) => {
    //     //console.log("before set function" + clickedPerson)
    //     setClickedPerson(e.target.innerHTML)
    //     //console.log("after set function" + clickedPerson)

    // };