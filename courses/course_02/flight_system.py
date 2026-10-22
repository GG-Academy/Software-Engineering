# Flight Information System
# Software Engineering - SDLC Practical Exercise

# PHASE 1: REQUIREMENTS
# The system must: 1) display flights, 2) search by destination, 3) display a message if no flight is found.

# PHASE 2: DESIGN
# Each flight has an ID, origin, destination, and price.

# PHASE 3: IMPLEMENTATION
flights = [
    {
        "id": "F101",
        "origin": "Bucharest",
        "destination": "London",
        "price": 120
    },
    {
        "id": "F102",
        "origin": "Bucharest",
        "destination": "Rome",
        "price": 85
    },
    {
        "id": "F103",
        "origin": "Bucharest",
        "destination": "Paris",
        "price": 150
    },
    {
        "id": "F104",
        "origin": "Rome",
        "destination": "Paris",
        "price": 60
    }
]

def display_flights():
    print("\n--- AVAILABLE FLIGHTS ---")
    for flight in flights:
        print(
            f"{flight['id']} | "
            f"{flight['origin']} -> "
            f"{flight['destination']} | "
            f"EUR {flight['price']}"
        )

def search_flights():
    destination = input(
        "\nEnter destination: "
    ).strip().lower()
    found = False
    for flight in flights:
        if flight["destination"].lower() == destination:
            print(
                f"Flight found: {flight['id']} | "
                f"{flight['origin']} -> "
                f"{flight['destination']} | "
                f"EUR {flight['price']}"
            )
            found = True
    if not found:
        print("No flights found.")

# PHASE 4: TESTING
# Students will manually test the application, and add their own real flight in the "dataset".

# PHASE 5: DEPLOYMENT
# Run the program using Python. Check if your flight is shown.

def main():
    while True:
        print("\n= FLIGHT INFORMATION SYSTEM =")
        print("1. Display flights")
        print("2. Search flights")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            display_flights()
        elif choice == "2":
            search_flights()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
