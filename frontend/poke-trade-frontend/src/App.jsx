import React, {useState, useEffect} from "react";
import axios from "axios";

function App() {
    const [cards, setCards] = useState([]);


    useEffect(() => {
        axios.get("http://127.0.0.1:8000/cards/")
            .then(res => setCards(res.data))
            .catch(err => console.log(err));
    }, [])



    return (
        <div className="container mt-5">
            <h1>Pokemon cards</h1>
            <div>
                {cards.map((card, i) => (
                    <div key={i}>
                        <h2>{card.name}</h2>
                        <p>Card-series: {card.set_name}</p>
                        <img src={card.image_url} alt={card.name}/>
                        <p>Number: {card.number}</p>
                        <p>Rarity: {card.rarity}</p>
                        <p>Price: {card.price}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default App;