
if __name__ == "__main__":
    boardingPasses = [line for line in open("AdventOfCodeDay05.txt","r")]
    maxSeatId = 0
    for boardingPass in boardingPasses:
        rows = [ n for n in range(0,128)]
        for direction in boardingPass[0:7]:
            midPoint = int(len(rows)/2)
            if direction == "F":
                rows = rows[:midPoint]
            else:
                rows = rows[midPoint:]

        seats = [ s for s in range(0,8)]
        for direction in boardingPass[7:]:
            midPoint = int(len(seats)/2)
            if direction == "L":
                seats = seats[:midPoint]
            else:
                seats = seats[midPoint:]
        currSeatId = int(rows[0])*8+int(seats[0])
        if maxSeatId < currSeatId:
            maxSeatId = currSeatId

    print(f"Highest SeatId : {maxSeatId}")