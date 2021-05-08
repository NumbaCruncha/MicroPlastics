
import React, { Component } from 'react';
import { CardDeck, Card, Button} from 'react-bootstrap';
// import Table from 'react-bootstrap/Table';
import { render } from "react-dom";

class RecentObs extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/fieldwork")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          }
        })
      })
  }

  render() {    
    return (
      <div>
        <Card className="card-style" onClick={this.props.clicked}>
          <CardImg top width="100%" src={this.props.image} alt="Card image cap" />
          <CardBody>
            <CardTitle >{this.props.data.id}</CardTitle>
            <CardSubtitle>${this.props.data.datatime}</CardSubtitle>
            <CardText>{this.props.data.field_user}</CardText>
          </CardBody>
        </Card>
      </div>
      );
  }
}

export default RecentObs;
const container = document.getElementById("recent_obs");
render(<RecentObs />, container);





