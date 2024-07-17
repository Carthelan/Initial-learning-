import React, { useState, useEffect } from 'react';
import { OverviewContainer } from '../Resources/Themes/StyledComponents';
import { PersonSpecifics } from '../Resources/Themes/StyledComponents';


export default function MainInfo({flightData, clickedPerson}) {

    let name = clickedPerson[1]
    let flight = clickedPerson[0]

    return(
        <div>
            <OverviewContainer>

            </OverviewContainer>
            <div>{flight}, {name} </div>
            <PersonSpecifics>
                <div>
                    Trainings
                    <br/>

                </div>
                <div>
                    IMR
                </div>
            </PersonSpecifics>
        </div>
    )
}