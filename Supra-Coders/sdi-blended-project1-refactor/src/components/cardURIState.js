import React, { useState, useEffect } from 'react';

const CardURI = ({ card }) => {
    const [imageURL, setImageURL] = useState({})
    
    
    //setImageURL([
    //    cardData.map(element => {element.image_uris.normal})
    //])
    //props.map(element => {element.image_uris.normal})
    useEffect(() => {
        setImageURL(card.image_uris)
        //if (card.image_uris['normal'])  {
        //    setImageURL(card.image_uris['normal'])
        //}
    }, [])
    if (!imageURL['normal']) {
        //setImageURL({normal: "it's dead Jim"})
        return (
            <p>missing</p>
        )
    } else {
        return (
            <p>
                {console.log(imageURL['normal'])}
                {/* {card.image_uris >0? <h1>{card.image_uris.normal}</h1> : <h1>missing</h1>} */}
            </p>
        )
    }
    //if (Object.keys(imageURL).length === 0) {
    //    return (
    //        <p>
    //            shit aint here
    //        </p>
    //    )
    //} 
}

export default CardURI