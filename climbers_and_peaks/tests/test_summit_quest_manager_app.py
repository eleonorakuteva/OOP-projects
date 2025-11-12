import unittest
from project.summit_quest_manager_app import SummitQuestManagerApp


class TestSummitQuestManagerApp(unittest.TestCase):

    def setUp(self):
        self.app = SummitQuestManagerApp()

    def test_register_climber_success(self):
        result = self.app.register_climber("ArcticClimber", "Alice")
        self.assertEqual(result, "Alice is successfully registered as a ArcticClimber.")
        self.assertEqual(len(self.app.climbers), 1)

    def test_register_climber_duplicate(self):
        self.app.register_climber("SummitClimber", "Bob")
        result = self.app.register_climber("SummitClimber", "Bob")
        self.assertEqual(result, "Bob has been already registered.")
        self.assertEqual(len(self.app.climbers), 1)

    def test_register_invalid_climber_type(self):
        result = self.app.register_climber("OceanClimber", "Liam")
        self.assertEqual(result, "OceanClimber doesn't exist in our register.")

    def test_peak_wish_list_success(self):
        result = self.app.peak_wish_list("ArcticPeak", "Everest", 4000)
        self.assertEqual(result, "Everest is successfully added to the wish list as a ArcticPeak.")
        self.assertEqual(len(self.app.peaks), 1)

    def test_peak_wish_list_invalid_type(self):
        result = self.app.peak_wish_list("UnknownPeak", "Mystery", 3000)
        self.assertEqual(result, "UnknownPeak is an unknown type of peak.")

    def test_check_gear_prepared(self):
        self.app.register_climber("ArcticClimber", "Alice")
        self.app.peak_wish_list("ArcticPeak", "Everest", 4000)

        gear = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
        result = self.app.check_gear("Alice", "Everest", gear)
        self.assertEqual(result, "Alice is prepared to climb Everest.")
        self.assertTrue(self.app.climbers[0].is_prepared)

    def test_check_gear_missing(self):
        self.app.register_climber("ArcticClimber", "Alice")
        self.app.peak_wish_list("ArcticPeak", "Everest", 4000)

        gear = ["Ice axe", "Crampons"]  # Missing items
        result = self.app.check_gear("Alice", "Everest", gear)
        self.assertIn("Missing gear:", result)
        self.assertFalse(self.app.climbers[0].is_prepared)

    def test_perform_climbing_success(self):
        self.app.register_climber("SummitClimber", "Bob")
        self.app.peak_wish_list("SummitPeak", "K2", 2500)
        gear = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        self.app.check_gear("Bob", "K2", gear)

        result = self.app.perform_climbing("Bob", "K2")
        self.assertIn("conquered K2", result)
        self.assertEqual(self.app.climbers[0].conquered_peaks, ["K2"])

    def test_perform_climbing_unprepared(self):
        self.app.register_climber("SummitClimber", "Bob")
        self.app.peak_wish_list("SummitPeak", "K2", 2500)
        # mark unprepared
        self.app.climbers[0].is_prepared = False

        result = self.app.perform_climbing("Bob", "K2")
        self.assertEqual(result, "Bob will need to be better prepared next time.")

    def test_perform_climbing_climber_not_found(self):
        self.app.peak_wish_list("SummitPeak", "K2", 2500)
        result = self.app.perform_climbing("Unknown", "K2")
        self.assertEqual(result, "Climber Unknown is not registered yet.")

    def test_perform_climbing_peak_not_found(self):
        self.app.register_climber("SummitClimber", "Bob")
        result = self.app.perform_climbing("Bob", "UnknownPeak")
        self.assertEqual(result, "Peak UnknownPeak is not part of the wish list.")

    def test_get_statistics(self):
        self.app.register_climber("SummitClimber", "Bob")
        self.app.peak_wish_list("SummitPeak", "K2", 2500)
        gear = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
        self.app.check_gear("Bob", "K2", gear)
        self.app.perform_climbing("Bob", "K2")

        stats = self.app.get_statistics()
        self.assertIn("Total climbed peaks: 1", stats)
        self.assertIn("Bob", stats)


if __name__ == "__main__":
    unittest.main()
