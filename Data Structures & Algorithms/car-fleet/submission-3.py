class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        last_time = 0
        fleets = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            
            if time > last_time:
                fleets += 1
                last_time = time
                
            
        return fleets