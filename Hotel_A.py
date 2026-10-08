from datetime import datetime, timezone
import calendar


# ==========================================================
class Room():

    room_id_counter = 0

    def __init__(self, size):
        Room.room_id_counter += 1

        self.id = Room.room_id_counter
        self.size = size
        self.status = "free"

    def get_price(self):

        if self.size in [1, 2]:
            self.price = 200
            return self.price

        elif self.size in [3, 4]:
            self.price = 300
            return self.price

        elif self.size >= 5 and self.size < 7:
            self.price = 500
            return self.price

        else:
            return 0


# ==========================================================
class Booking:

    book_id_counter = 0

    def __init__(self, room, customer_name, expire_date):

        Booking.book_id_counter += 1

        self.id = Booking.book_id_counter
        self.room = room
        self.customer_name = customer_name
        self.date = datetime.now(timezone.utc)
        self.price = room.get_price()
        self.expire_date = expire_date

        room.status = "busy"


# ==========================================================
class Hotel:

    def __init__(self):
        self.rooms = []
        self.bookings = []

# ======================================================
    def add_room(self):
        try:
            size = int(input("Enter Size: "))

        except ValueError:
            print("Enter a Number")
            return

        if size > 7:
            print("Maximum size is 7")
            return

        elif size <= 0:
            print("Minimum size is 1")
            return

        room = Room(size)
        self.rooms.append(room)

        print(f"Room {room.id} added successfully")

# ======================================================
    def find_room(self):

        try:
            find_id = int(input("Enter ID: "))

        except ValueError:
            print("Enter a Number")
            return

        for room in self.rooms:

            if room.id == find_id:
                return room

        print("Not Found")
        return None

# ======================================================
    def show_rooms(self):

        show_cond = input(
            "Enter True/False To see All Rooms: "
        ).lower()

        if show_cond == "false":
            print("Thank You")

        elif show_cond == "true":

            for room in self.rooms:
                print(
                    f"Room ID: {room.id} | "
                    f"Room Size: {room.size} | "
                    f"Room Status: {room.status}"
                )

# ======================================================
    def show_free_rooms(self):

        free_cond = input(
            "Enter Y/N To see Free Rooms: "
        ).lower()

        if free_cond == "n":
            print("Thank You")

        elif free_cond == "y":

            counter = 0

            for room in self.rooms:

                if room.status == "free":

                    counter += 1

                    print(
                        f"Free Rooms: {counter} | "
                        f"Room ID: {room.id} | "
                        f"Room Size: {room.size} | "
                        f"Room Status: {room.status}"
                    )

            if counter == 0:
                print("No free rooms found.")

# ======================================================
    def show_busy_rooms(self):

        b_counter = 0

        busy_cond = input(
            "Enter Y/N To see Busy Rooms: "
        ).lower()

        if busy_cond == "y":

            for room in self.rooms:

                if room.status == "busy":

                    b_counter += 1

                    print(
                        f"Busy Rooms: {b_counter} | "
                        f"Room ID: {room.id} | "
                        f"Room Size: {room.size} | "
                        f"Room Status: {room.status}"
                    )

            if b_counter == 0:
                print(
                    f"Not Found, Total busy rooms: {b_counter}"
                )

        elif busy_cond == "n":
            print("Thank you")

# ======================================================
    def create_book(self):

        today = datetime.now()

        year = today.year
        month = today.month
        day = today.day
        future_month = month + 2
        future_year = year

        if future_month > 12:
            future_year += 1
            future_month -= 12

        max_book_date = datetime(
            future_year,
            future_month,
            day
        )
        customer_name = input(
            "Enter Your Name: "
        ).strip()

        if customer_name == "":
            print("Name cannot be empty")
            return

        try:
            room_id = int(
                input("Enter a Room ID: ")
            )

        except ValueError:
            print("Enter a Number")
            return
        
        room = None

        for i in self.rooms:

            if i.id == room_id:
                room = i
                break

        if room is None:
            print("Not Found")
            return

        if room.status == "busy":
            print("The Room is Busy Right Now")
            return

        print(
            f"Today Date is: "
            f"{today.strftime('%Y/%m/%d')}"
        )

        print(
            f"Maximum Book Date is: "
            f"{max_book_date.strftime('%Y/%m/%d')}"
        )

        try:

            ep_month = int(
                input(f"Enter Month: {year}/")
            )

            ep_day = int(
                input(
                    f"Enter Day: "
                    f"{year}/{ep_month}/"
                )
            )

        except ValueError:

            print("Enter a Number")
            return
        
        if ep_month < 1 or ep_month > 12:

            print("Invalid Month")
            return

        days_in_month = calendar.monthrange(
            year,
            ep_month
        )[1]

        if ep_day < 1 or ep_day > days_in_month:

            print("Invalid Day")
            return

        expire_date = datetime(
            year,
            ep_month,
            ep_day
        )

        if expire_date < today:

            print(
                "Expire date cannot be before today"
            )
            return

        if expire_date > max_book_date:

            print(
                "Expire date cannot be more than 2 months"
            )
            return

        booking = Booking(
            room,
            customer_name,
            expire_date
        )

        self.bookings.append(booking)

        print("Success")


hotel = Hotel()

print("Hello There !")
print('Add_room = 1 \t' \
'show room = 2 \t' \
'show free rooms = 3 \t' \
'show busy rooms = 4 \t' \
'create a book = 5 \t' \
'find room = 6 \t' \
'EXIT... = 0 '
)


while True :
    request = input('What You want me to do ? (0,6) : ')

    if request == "1" :
        hotel.add_room()

    elif request == "2" :
        hotel.show_rooms()

    elif request == "3" :
        hotel.show_free_rooms()

    elif request == "4" :
        hotel.show_busy_rooms()

    elif request == "5" :
        hotel.create_book()

    elif request == "6" :
        hotel.find_room()

    elif int(request) > 6:
        print('invalid number')
        
    else :
        break