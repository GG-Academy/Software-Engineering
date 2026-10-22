# Software Development Life Cycle (SDLC)

This lab activity shows how Software Development Life Cycle works using a simple didactic example of an aviation-related app.

Your task is to analyze the details below and the provided code. Also, you have to introduce a new real flight and run the code. Upload on Moodle the modified code.

## Flight Information System

The code contains the implementation of a flight information system. This was done using an iterative process.

### Scenario

An airline has a small software program that displays flights and searches for flights by destination. The system only supports direct flights at the moment.

### Application features

After anaylizing the client's requests, the software development team identified the following requests: 

1. Display all available flights.
2. Search for flights by destination.
3. Display a message if no flight is found.

### Task

The code in `flight_system.py` contains the implementation of this app. Check the code and understand each of the 5 PHASES. You will work at PHASE 4 for the moment and will have to run the code on your laptop. You must add a real flight from any airport in the world - make sure to include the proper flight ID, the real origin, destionation, and a price taken from a booking platform. Make sure the system can find your flight using the search function and upload the modified code on Moodle.

Notice that each flight has the following structure provided as a dictionary in Python:
```
{
    "id": "F101",
    "origin": "Bucharest",
    "destination": "London",
    "price": 120
}
```

Before runing the code, updated the list of `flights` in the code and introduce a real flight which you will extract from a flight booking app. 
