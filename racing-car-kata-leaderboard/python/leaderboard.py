from typing import Dict, List


class LeaderBoard:
    def __init__(self, drivers: List[str]):
        self.__drivers: List[str] = drivers
        self.__board: Dict[str, int] = {}
        self.__set_drivers_with_0_points()
    def __set_drivers_with_0_points(self):
        for driver in self.__drivers:
            self.__board.update({driver: 0})

    def pointsOf(self, driver: str):
        return self.__board.get(driver)

    def race(self, drivers: List[str]):
        points = [10, 8, 6, 4, 2, 1]
        for index, driver in enumerate(drivers):
            if index < len(points):
                self.__board.update({driver: self.pointsOf(driver) + points[index]})
