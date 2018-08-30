class SeatingChart:

    def __init__(self, rows, seats):
        self.chart = [[0 for i in range(seats)] for j in range(rows)]

    def ReserveSeat(self, row, seat):
        if row > 0 and seat > 0 and row <= len(self.chart) and seat <= len(self.chart[row - 1]):
            self.chart[row - 1][seat - 1] = 1
    
    def CheckSeatReserved(self, row, seat):
        if row > 0 and seat > 0 and row <= len(self.chart) and seat <= len(self.chart[row - 1]):
            return self.chart[row - 1][seat - 1]
        else:
            return 0