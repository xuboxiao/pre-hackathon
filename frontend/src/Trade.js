import React, { Component } from "react";
import Form from "./Form"

class Trade extends Component{
    state = {
        characters: []
    };

    removeCharacter = index => {
        const { characters } = this.state;
    
        this.setState({
            characters: characters.filter((character, i) => { 
                return i !== index;
            })
        });
    }

    handleSubmit = character => {
        this.setState({characters: [...this.state.characters, character]});
    }

    render(){
        const { characters } = this.state;
        return(
            <div className="container">
                <h1>Initiate Trade</h1>
                <hr/>
                <h3>Buy/Sell</h3>
                <Form handleSubmit={this.handleSubmit} />
            </div>
        );
    }

}
export default Trade;