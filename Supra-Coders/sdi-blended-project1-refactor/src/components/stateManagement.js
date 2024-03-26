import React, { useState, useEffect } from 'react';
import CardURI from './cardURIState';

const CardState = () => {
    const [searchURL, setSearchURL] = useState({
        url: 'https://api.scryfall.com/cards/search?q=t:knight&c:w&m:2'
        }) //re-render page when this changes
    const [cardData, setCardData] = useState([])
    //const [imageURL, setImageURL] = useState("random shit")

    useEffect(() => {
        fetch(searchURL.url)
            .then(res => res.json())
            .then(res => res['data'])
            .then(data => {
                setCardData(data)
                //console.log(data)
                //setImageUrl(data.image_uri.normal)
            })
    }, [searchURL]) //re-render page when searchURL changes 
    //if ()


    return(
        <>
            {/* {imageURL} 
            <img src=''/> */}
            {/* {cardData.map(element => <h1>{element.image_uris.normal}</h1>)} */}
            {/* <CardURI cardData={cardData} /> */}
            {cardData.map(card => <CardURI card={card} />)}
        </>
    )
}


export default CardState

//make a new URL state. Every input field will { (I need react routing actually. Potentially)
// ...URL state string
//      += (string logic) & new url fragment 
//}