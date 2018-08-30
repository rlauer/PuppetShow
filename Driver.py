from SeatingChart import SeatingChart, Seat

CHART_ROWS = 3
CHART_SEATS = 11

# Get the row and seat out of the input string
def parseReservation(reservation):
    (row, seat) = reservation.strip('R').split('C')
    return (int(row), int(seat))


# Initialize Chart
chart = SeatingChart(CHART_ROWS, CHART_SEATS)


# Initial Reservations
reservationInput = input()

reservations = []
for reservation in reservationInput.split(' '):
    (row, seat) = parseReservation(reservation)
    chart.ReserveSeat(row, seat)


# Find Best Seats
while True:
    numSeats = input()
    if numSeats:
        seats = chart.FindBestSeats(int(numSeats))
        if seats == -1:
            print("Not Available")
        elif len(seats) == 1:
            seat = seats[0]
            chart.ReserveSeat(seat[0], seat[1])
            print(f"R{seat[0]}C{seat[1]}")
        else:
            for seat in seats:
                chart.ReserveSeat(seat[0], seat[1])
            seats.sort(key = lambda s: s[1]) # order by seat
            rowNumber = seats[0][0]
            print(f"R{rowNumber}C{seats[0][1]} - R{rowNumber}C{seats[len(seats) - 1][1]}")
    else:
        print(chart.TotalUnreservedSeats())
        break


# Show reserved seats (for debugging)
# for i in range(CHART_ROWS):
#     print(f"{i + 1}: {['X' if seat.reserved else 'O' for seat in chart.chart[i]]}")