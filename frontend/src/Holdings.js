import React, { Component } from "react";
import { Doughnut } from "react-chartjs-2";
import "./index.css";


class Holdings extends Component {

    state = {
        dataDoughnut: {
            labels: ["Rubber Company", "Solar Company", "Oil Company", "Plantation Company", "Mining Company"],
            datasets: [
                {
                    data: [300, 50, 100, 40, 120],
                    backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"],
                    hoverBackgroundColor: [
                        "#FF5A5E",
                        "#5AD3D1",
                        "#FFC870",
                        "#A8B3C5",
                        "#616774"
                    ]
                }
            ]
        }
    }

    render() {

        return (
            <div className="container">
                    <h3 className="mt-5">Holdings Status</h3>
                    <Doughnut data={this.state.dataDoughnut} options={ { responsive: true }} />
            </div>
        );
    }

}
export default Holdings;