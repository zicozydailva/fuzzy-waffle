TASKS_DEV = [
    Task(
        annotator="0",
        user_id="guest",
        instruction="your name is Billy Bob. you are a very private person and don\'t like providing personal information to others, so you want to continue as guest rather than creating an account. you live in SEA and want to book a 2-night staycation for you and the your partner in a deluxe room starting on April 23rd using credit_card_9568. You have elite status with Marriott so you want to book in a Marriott hotel if that\'s available. Don\'t book anything other than what is in these instructions.",
        actions=[
            Action(
                name="book_hotel",
                kwargs={
                    "user_id": "guest",
                    "hotel_id": "M1",
                    "hotel_city": "SEA",
                    "hotel_chain": "Marriott",
                    "room_types": ["deluxe"],
                    "check_in_date": "2025-04-23",
                    "check_out_date": "2025-04-25",
                    "num_guests": 2,
                    "payment_id": "credit_card_9568",
                    "total_cost": 600,
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="0",
        user_id="lumon_lady",
        instruction="Your name is Helena Eagan. Your email is kier4eva@hotmail.com. Your zip code is 67143 and your phone number is 7235569287. The payment method you have on file is credit_card_0455. You want to fly from ATL to SEA with your father for vacation. You want to arrive in SEA on May 7 and depart on May 11. You want to fly first class and you\'ll have 6 suitcases. You don\'t want travel insurance. You will want lodging while you\'re in SEA for 4 nights, but only mention that after the flights are booked. You want to stay in a deluxe room and don\'t have any preferred hotel chain. You\'re pretty sure that your user_id is lumon_lady but you don\'t know your pin so you\'ll need to reset it. If lumon_lady happens not to work, try to see if your user_id is something else. If they don\'t find a user_id for you, it\'s possible that\'s because you did your last booking as guest and you\'ll need to create an account.  Use the PIN 4055. Don\'t book anything other than what is in these instructions.",)
        actions=[
            Action(
                name="reset_user_pin",
                kwargs={
                    "user_id": "lumon_lady",
                    "payment_id": "credit_card_0455",
                    "email_address": "kier4eva@hotmail.com",
                    "zip_code": 67143,
                    "phone_number": "7235569287",
                    "pin": 4055,
                },
            ),
            Action(
                name="create_user_account",
                kwargs={
                    "user_id": "lumon_lady",
                    "pin": 4055,
                    "first_name": "Helena",
                    "last_name": "Eagan",
                    "email_address": "kier4eva@hotmail.com",
                    "zip_code": 67143,
                    "phone_number": "7235569287",
                },
            ),
            Action(
                name="book_transport",
                kwargs={
                    "user_id": "lumon_lady",
                    "origin": "ATL",
                    "destination": "SEA",
                    "transport_type": "plane",
                    "trip_id": "P8",
                    "travel_class": "first",
                    "departure_date": "2025-05-07",
                    "departure_time": "08:00",
                    "arrival_date": "2025-05-07",
                    "arrival_time": "14:00",
                    "num_passengers": 2,
                    "payment_id": "credit_card_0455",
                    "total_bags": 6,
                    "nonfree_bags": 2,
                    "insurance": "no",
                    "total_cost": 6100,
                },
            ),
            Action(
                name="book_transport",
                kwargs={
                    "user_id": "lumon_lady",
                    "origin": "SEA",
                    "destination": "ATL",
                    "transport_type": "plane",
                    "trip_id": "P9",
                    "travel_class": "first",
                    "departure_date": "2025-05-11",
                    "departure_time": "20:00",
                    "arrival_date": "2025-05-12",
                    "arrival_time": "02:00",
                    "num_passengers": 2,
                    "payment_id": "credit_card_0455",
                    "total_bags": 6,
                    "nonfree_bags": 2,
                    "insurance": "no",
                    "total_cost": 7100,
                },
            ),
            Action(
                name="book_hotel",
                kwargs={
                    "user_id": "lumon_lady",
                    "hotel_id": "H1",
                    "hotel_city": "SEA",
                    "hotel_chain": "Hilton",
                    "room_types": ["deluxe"],
                    "check_in_date": "2025-05-07",
                    "check_out_date": "2025-05-11",
                    "num_guests": 2,
                    "payment_id": "credit_card_0455",
                    "total_cost": 6400,
                },
            ),
        ],
        outputs=[],
    Task(
        annotator="0",
        user_id="rachelismylobster",
        instruction="Your name is Ross Gellar. Your username is rachelismylobster and your PIN is 1999. You have booked a roundtrip from NYC to DEN through the agency. When you were booking the flights, you didn\'t realize that you were being charged $100 per flight for checked luggage. You want to change the number of bags on both flights so that they equal the total number of possible free bags according to policy (be sure to ask the the agent how many bags are possible because you don\'t know). You also want to book 1 suite and 1 standard room in the same hotel for your party of 5 in DEN for the length of your stay there; if there are multiple possible hotels select the cheapest combination. Don\'t book anything other than what is in these instructions.",
        actions=[
            Action(
                name="update_trip_reservation_bags",
                kwargs={
                    "reservation_id": "rachelismylobster_t_1",
                    "trip_id": "P10",
                    "new_total_bags": 5,
                    "new_nonfree_bags": 0,
                    "payment_id": "credit_card_6275",
                    "new_total_cost": 2500,
                    "old_total_cost": 2600,
                    "amount_charged": -100,
                },
            ),
            Action(
                name="update_trip_reservation_bags",
                kwargs={
                    "reservation_id": "rachelismylobster_t_2",
                    "trip_id": "P11",
                    "new_total_bags": 5,
                    "new_nonfree_bags": 0,
                    "payment_id": "credit_card_6275",
                    "new_total_cost": 3000,
                    "old_total_cost": 3100,
                    "amount_charged": -100,
                },
            ),
            Action(
                name="book_hotel",
                kwargs={
                    "user_id": "rachelismylobster",
                    "hotel_id": "H2",
                    "hotel_city": "DEN",
                    "hotel_chain": "Hilton",
                    "room_types": ["standard", "suite"],
                    "check_in_date": "2025-05-01",
                    "check_out_date": "2025-05-08",
                    "num_guests": 5,
                    "payment_id": "credit_card_6275",
                    "total_cost": 2100,
                }
            )
        ]
        outputs=[]
    )
]
