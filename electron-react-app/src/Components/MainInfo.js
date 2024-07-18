import React, { useState, useEffect } from 'react';
import { MainInfoContainer, 
        PersonSpecifics, 
        OverviewContainer, 
        TrainingContainer, 
        IMRContainer} from '../Resources/Themes/StyledComponents';


export default function MainInfo({flightData, clickedPerson}) {

    let name = clickedPerson[1]
    let flight = clickedPerson[0]
    let cbts = flightData[flight][name]["Trainings"]["CBTs"]

    function mappingFunction(specificTraining) {
        let allTrainings = Object.keys(flightData[flight][name]["Trainings"]) //array
        let allIMR = Object.keys(flightData[flight][name]["IMR"]) //array

        let imrCategories = flightData[flight][name]["IMR"] //object
        let trainings = flightData[flight][name]["Trainings"] //object

        allTrainings.map((specificTraining) => {
        if (specificTraining === "CBTs") {
            return (
                allTrainings.map((specificTraining) => (
                    <li>Hello</li>
                ))
            )
        } else {
            return (
                allTrainings.map((specificTraining) => (
                    <li>{specificTraining} {Object.values(trainings[specificTraining])}</li>
                ))
            )
        }})
    }


    if (clickedPerson.length < 1) {
        return(
            <>
                Please Select an indivudal Guardian
            </>
        )
    } else {
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
                            <ol style={{listStyle: 'none'}}>
                                {mappingFunction}
                            </ol>
                        </TrainingContainer>
                        <IMRContainer>
                            IMR
                            <br/>
                            <ol style={{listStyle: 'none'}}>
                                {mappingFunction}
                            </ol>
                        </IMRContainer>
                    </PersonSpecifics>
                </MainInfoContainer>
            </div>
        )
    }
}