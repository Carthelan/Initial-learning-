import React, { useState, useEffect } from 'react';
import { MainInfoContainer, 
        PersonSpecifics, 
        OverviewContainer, 
        TrainingContainer, 
        IMRContainer} from '../Resources/Themes/StyledComponents';



export default function MainInfo({flightData, clickedPerson}) {

    let name = clickedPerson[1]
    let flight = clickedPerson[0]


    if (clickedPerson.length < 1) {
        return(
            <>
                Please Select an indivudal Guardian
            </>
        )
    } else {
        let alltrainings = Object.keys(flightData[flight][name]["Trainings"])
        let allIMR = Object.keys(flightData[flight][name]["IMR"])
        let imrCategories = flightData[flight][name]["IMR"]
        let trainings = flightData[flight][name]["Trainings"]

        console.log(trainings)
        return(
            <div>
                <OverviewContainer>
                    some stuff in here 
                </OverviewContainer>
                <MainInfoContainer>
                    {flight}: {name} 
                    <PersonSpecifics>
                        <TrainingContainer>
                            Trainings
                            <br/>
                            <ul>
                                {alltrainings.map((training) => (
                                    <li>{training}</li>
                                ))}
                            </ul>
                        </TrainingContainer>
                        <IMRContainer>
                            IMR
                            <br/>
                            <ul>
                                {allIMR.map((indivualIMR) => (
                                    <li>{indivualIMR}</li>
                                ))}
                            </ul>
                        </IMRContainer>
                    </PersonSpecifics>
                </MainInfoContainer>
            </div>
        )
    }
}