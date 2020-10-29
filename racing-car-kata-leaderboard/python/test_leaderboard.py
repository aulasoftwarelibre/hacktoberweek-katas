import unittest

from leaderboard import LeaderBoard


class LeaderBoardTest(unittest.TestCase):
    def test_a_new_leaderboard_has_a_driver_with_zero_points(self):
        driver = "Charles Leclerc"

        leaderboard = LeaderBoard([driver])

        self.assertEqual(leaderboard.pointsOf(driver), 0)

    def test_a_new_leaderboard_has_many_drivers_with_zero_points(self):
        driver1 = "Charles Leclerc"
        driver2 = "Fernando Alonso"

        drivers = [driver1, driver2]

        leaderboard = LeaderBoard(drivers)

        self.assertEqual(leaderboard.pointsOf(driver1), 0)
        self.assertEqual(leaderboard.pointsOf(driver2), 0)

    def test_after_the_first_race_the_first_driver_has_10_points(self):
        first_driver = "Charles Leclerc"
        other_driver = "Fernando Alonso"
        drivers = [first_driver, other_driver]
        leaderboard = LeaderBoard(drivers)

        leaderboard.race(drivers)

        self.assertEqual(leaderboard.pointsOf(first_driver), 10)

    def test_after_the_first_race_the_6_first_pilots_have_the_correct_points_and_the_seventh_has_0_points(self):
        first_driver = "Alex Zanardi"
        second_driver = "Ayrton Senna"
        third_driver = "Nigel Mansell"
        fourth_driver = "Alain Prost"
        fifth_driver = "Michael Schumacher"
        sixth_driver = "Damon Hill"
        seventh_driver = "Mika Hakkinen"
        drivers = [first_driver, second_driver, third_driver, fourth_driver, fifth_driver, sixth_driver, seventh_driver]
        leaderboard = LeaderBoard(drivers)

        leaderboard.race(drivers)

        self.assertEqual(leaderboard.pointsOf(first_driver), 10)
        self.assertEqual(leaderboard.pointsOf(second_driver), 8)
        self.assertEqual(leaderboard.pointsOf(third_driver), 6)
        self.assertEqual(leaderboard.pointsOf(fourth_driver), 4)
        self.assertEqual(leaderboard.pointsOf(fifth_driver), 2)
        self.assertEqual(leaderboard.pointsOf(sixth_driver), 1)
        self.assertEqual(leaderboard.pointsOf(seventh_driver), 0)

    def test_that_after_multiple_races_the_drivers_have_points_accumulated(self):
        driver_1 = "Alex Zanardi"
        driver_2 = "Ayrton Senna"
        driver_3 = "Michael Schumacher"
        drivers = [driver_1, driver_2, driver_3]
        leaderboard = LeaderBoard(drivers)

        leaderboard.race([driver_3, driver_2, driver_1])
        leaderboard.race([driver_2, driver_1, driver_3])
        leaderboard.race([driver_3, driver_1, driver_2])

        self.assertEqual(leaderboard.pointsOf(driver_1), 22)
        self.assertEqual(leaderboard.pointsOf(driver_2), 24)
        self.assertEqual(leaderboard.pointsOf(driver_3), 26)
