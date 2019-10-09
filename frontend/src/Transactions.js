import React, { Component } from "react";
import Table from "./Table"

class Transactions extends Component{
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
        const characters = [
            {
              asset: 'Rubber Company',
              quantity: '300',
              date:'2019-01-20'
            },
            {
                asset: 'Solar Company',
                quantity: '50',
                date:'2019-02-12'
            },
            {
                asset: 'Oil Company',
                quantity: '100',
                date:'2019-03-14'
            },
            {
                asset: 'Plantation Company',
                quantity: '40',
                date:'2019-04-30'
            },
            {
                asset: 'Mining Company',
                quantity: '120',
                date:'2019-05-21'
            },
          ]
        //const { characters } = this.state;
        return(
            <div className="container">
                <h1>Transactions Summary</h1>
                <br/>
                <Table
                    characterData={characters}
                />
            </div>
        );
    }

}
export default Transactions;