class Best_elevator():
    def __init__(self, count_floor=5, now_floor=3):
        self.count_floor = count_floor
        self.now_floor = now_floor
    def elevator_up(self, count_floor, now_floor):
        if now_floor < count_floor:
            now_floor += 1
            print("Elevator upped to ", now_floor, "floor")
        else:
            print("Elevator can't up")
    def elevator_down(self, now_floor):
        if now_floor != 1:
            now_floor -= 1
            print("Elevator get down to ", now_floor, "floor")
        else:
            print("Elevator can't get down")

    def move(self, count_floor, you_move):
        if you_move > 1 or you_move < count_floor:
            now_floor = you_move
            print("Elevator came to ", now_floor, "floor")
        else:
            print("wrong floor number")
elevator = Best_elevator()
elevator.move(7, 5)
