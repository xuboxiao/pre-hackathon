import React from 'react';
import {
  Jumbotron,
  Container,
  Row,
  Col
} from 'reactstrap';
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";
import Wallet from "./Wallet";
import Holdings from "./Holdings";
import Transactions from "./Transactions";
import Trade from "./Trade";
import './App.css';

export default class App extends React.Component {
  render() {
    return (
      <div>
        <h1>DB Eco App</h1>
        
        <HashRouter>
          <ul className="header">
            <li><img src="./dbecologo.jpg" height="52" width="50"/></li>
            <li><NavLink to="/wallet">Wallet</NavLink></li>
            <li><NavLink to="/holdings">Holdings</NavLink></li>
            <li><NavLink to="/transactions">Transactions</NavLink></li>
            <li><NavLink to="/trade">Trade</NavLink></li>
          </ul>
          <div className="content" >
            <Route path="/wallet" component={Wallet} />
            <Route path="/holdings" component={Holdings} />
            <Route path="/transactions" component={Transactions} />
            <Route path="/trade" component={Trade} />
          </div>
        </HashRouter>
        <div id="footerContainer"  class="w3-row-padding w3-margin-bottom ">
    <footer class="page-footer  fixed-bottom text-center footerContainer">
    &copy;Deutsche Bank Singapore Hackathon, 2019

   <a href="https://twitter.com" target="_blank" class="fa fa-twitter"></a>
   <a href="https://google.com" class="fa fa-google"></a>
   <a href="https://linkedin.com" class="fa fa-linkedin"></a>

</footer>
</div>
      </div>
      
    );
  }
};
