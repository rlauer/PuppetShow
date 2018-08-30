from SeatingChart import SeatingChart

CHART_ROWS = 3
CHART_SEATS = 11

def parseReservation(reservation):
    (row, seat) = reservation.strip('R').split('C')
    return (int(row), int(seat))

chart = SeatingChart(CHART_ROWS, CHART_SEATS)

reservationInput = input()
seatList = []
while True:
    numSeats = input()
    if numSeats:
        seatList.append(int(numSeats))
    else:
        break

reservations = []
for reservation in reservationInput.split(' '):
    (row, seat) = parseReservation(reservation)
    chart.ReserveSeat(row, seat)


print(seatList)

for i in range(CHART_ROWS):
    print(f"{i + 1}: {chart.chart[i]}")