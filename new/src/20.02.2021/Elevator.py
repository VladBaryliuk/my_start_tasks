class Elevator():
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
            print("Elevator can't grt down")
elevator = Elevator(count_floor=6, now_floor=5)
elevator.elevator_up(count_floor=6, now_floor=5)
elevator.elevator_up(count_floor=6, now_floor=6)
elevator.elevator_down(now_floor=6)