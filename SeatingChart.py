class Seat:
    def __init__(self, distance):
        self.reserved = False
        self.distance = distance

class SeatingChart:
    distanceList = []


    def __init__(self, rows, seats):
        self.rows = rows
        self.seats = seats
        self.bestLocation = (1, (seats + 1) / 2.0)

        # Initialize seat array including availability and how ideal the location is
        self.chart = [
            [
                Seat(self.calculateManhattanDistance(i + 1, j + 1))
                for j in range(seats)
            ]
            for i in range(rows)
        ]

        # Create list of seats ordered by how ideal they are
        for row in range(rows):
            for seat in range(seats):
                self.distanceList.append((row + 1, seat + 1, self.calculateManhattanDistance(row + 1, seat + 1)))
        
        self.distanceList.sort(key=lambda seat: seat[2])


    def ReserveSeat(self, row, seat):
        if row > 0 and seat > 0 and row <= len(self.chart) and seat <= len(self.chart[row - 1]):
            self.chart[row - 1][seat - 1].reserved = True

    
    def CheckSeatReserved(self, row, seat):
        if row > 0 and seat > 0 and row <= len(self.chart) and seat <= len(self.chart[row - 1]):
            return self.chart[row - 1][seat - 1].reserved
        else:
            return False


    def TotalUnreservedSeats(self):
        totalSeats = 0
        
        for row in self.chart:
            for seat in row:
                if not seat.reserved: totalSeats += 1
        
        return totalSeats

    
    def calculateManhattanDistance(self, row, seat):
        (bestRow, bestSeat) = self.bestLocation
        return abs(bestRow - row) + abs(bestSeat - seat)


    def getManhattanDistance(self, row, seat):
        return self.chart[row - 1][seat - 1].distance


    def getSurroundingSeats(self, row, seat, numSeats):
        seatList = []

        # Check current seat and ones to the right
        for i in range(seat, self.seats + 1):
            if self.CheckSeatReserved(row, i):                
                break
            else:
                seatList.append((row, i, self.getManhattanDistance(row, i)))

        # Original seat was taken, exit
        if len(seatList) == 0: return []

        # Check seats to the left of current seat
        for i in range(seat - 1, 1, -1):
            if self.CheckSeatReserved(row, i):
                break
            else:
                seatList.append((row, i, self.getManhattanDistance(row, i)))

        return seatList

    
    def FindBestSeats(self, numSeats):
        # Iterate from best to worst seats
        for (row, seat, _) in self.distanceList:
            seats = self.getSurroundingSeats(row, seat, numSeats)
            if len(seats) == numSeats:
                return seats
            elif len(seats) > numSeats:
                seats.sort(key = lambda s: s[2])
                return seats[:numSeats]
        
        return -1

    