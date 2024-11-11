import unittest
from projectile_motion.projectile_motion import calculate_projectile_motion


class TestProjectileMotion(unittest.TestCase):

    # Horizontal Launch Tests
    def test_horizontal_launch(self):
        _, _, _, result = calculate_projectile_motion(velocity=20, angle=0, height=0)
        self.assertAlmostEqual(result["flight_time"], 0.0, places=2)
        self.assertAlmostEqual(result["max_height"], 0.0, places=2)
        self.assertAlmostEqual(result["horizontal_range"], 0.0, places=2)
        self.assertAlmostEqual(result["impact_velocity"], 20.0, places=2)
        self.assertAlmostEqual(result["impact_angle"], 0.0, places=2)

    # Angle Launch Tests
    def test_angle_launch_45_degrees(self):
        _, _, _, result = calculate_projectile_motion(velocity=20, angle=45, height=0)
        self.assertAlmostEqual(result["flight_time"], 2.88, places=2)
        self.assertAlmostEqual(result["max_height"], 10.19, places=2)
        self.assertAlmostEqual(result["horizontal_range"], 40.77, places=2)
        self.assertAlmostEqual(result["impact_velocity"], 20.0, places=2)
        self.assertAlmostEqual(result["impact_angle"], -45.0, places=1)

    def test_angle_launch_30_degrees(self):
        _, _, _, result = calculate_projectile_motion(velocity=25, angle=30, height=0)
        self.assertAlmostEqual(result["flight_time"], 2.55, places=2)
        self.assertAlmostEqual(result["max_height"], 7.96, places=2)
        self.assertAlmostEqual(result["horizontal_range"], 55.17, places=2)
        self.assertAlmostEqual(result["impact_velocity"], 25.0, places=2)
        self.assertAlmostEqual(result["impact_angle"], -30.0, places=1)

    # Free Fall Tests
    def test_free_fall_from_height(self):
        _, _, _, result = calculate_projectile_motion(velocity=0, angle=0, height=50)
        self.assertAlmostEqual(result["flight_time"], 3.19, places=2)
        self.assertAlmostEqual(result["max_height"], 50.0, places=2)
        self.assertAlmostEqual(result["horizontal_range"], 0.0, places=2)
        self.assertAlmostEqual(result["impact_velocity"], 31.3, places=1)
        self.assertAlmostEqual(result["impact_angle"], -90.0, places=1)

    # General Test with Height
    def test_launch_with_initial_height(self):
        _, _, _, result = calculate_projectile_motion(velocity=20, angle=45, height=10)
        self.assertAlmostEqual(result["flight_time"], 3.47, places=2)
        self.assertAlmostEqual(result["max_height"], 20.19, places=2)
        self.assertAlmostEqual(result["horizontal_range"], 49.08, places=2)
        self.assertAlmostEqual(result["impact_velocity"], 24.42, places=2)
        self.assertAlmostEqual(result["impact_angle"], -54.61, places=2)


if __name__ == "__main__":
    unittest.main()
