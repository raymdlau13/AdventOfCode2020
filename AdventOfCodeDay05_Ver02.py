
def convert_to_seat_id(boardingPass):
    return (int(boardingPass[:7],2)*8)+int(boardingPass[-3:],2)


if __name__ == "__main__":
    seatIDs = [convert_to_seat_id(boardingPass.translate(boardingPass.maketrans("FBLR","0101")).strip()) 
                for boardingPass in open("AdventOfCodeDay05.txt","r")]

    for seatId in seatIDs:
        if (seatId + 2 in seatIDs and  seatId + 1 not in seatIDs) \
        or (seatId - 2 in seatIDs and seatId - 1 not in seatIDs):
            print(f"my seatId is : {seatId+1}") 
            break

    print(f"Highest Seat Id: {max(seatIDs)}")