import React, { Component } from 'react';
import { CardDeck, Card, Button } from 'react-bootstrap';
import { render } from "react-dom";

const Number = 1
 
function InfoCard() {
  return (
<CardDeck>
<Card>
  <Card.Header as="h4">Featured</Card.Header>
  <Card.Body>
    <Card.Title>Item #{ Number }</Card.Title>
    <Card.Text>
      With supporting text below as a natural lead-in to additional content.
    </Card.Text>
    <Button variant="primary">Go somewhere</Button>
  </Card.Body>
</Card>
<Card>
  <Card.Header as="h4">Featured</Card.Header>
  <Card.Body>
    <Card.Title>Item #{ Number + 1}</Card.Title>
    <Card.Text>
      With supporting text below as a natural lead-in to additional content.
    </Card.Text>
    <Button variant="primary">Go somewhere</Button>
  </Card.Body>
</Card>
</CardDeck>
  )
}

const container2 = document.getElementById("infocard");
render(<InfoCard />, container2);