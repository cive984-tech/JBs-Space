import unittest
from agent import AutonomousAgent

class TestAutonomousAgent(unittest.TestCase):

    def setUp(self):
        # Initialize the agent before each test
theace.    self.agent = AutonomousAgent(max_iterations=10)

    def test_initialization(self):
        self.assertIsInstance(self.agent, AutonomousAgent)
        self.assertEqual(self.agent.max_iterations, 10)

    def test_iteration_limits(self):
        # Test the agent's response when max iterations are reached
        for _ in range(10):
            self.agent.iterate()
        self.assertRaises(Exception, self.agent.iterate)

    def test_error_handling(self):
        # Simulate an error and verify the agent handles it
        with self.assertRaises(ValueError):
            self.agent.process_data(None)

    def test_logging(self):
        # Test if logging works correctly
        self.agent.iterate()
        self.assertIn("Iteration completed.", self.agent.logs)

if __name__ == '__main__':
    unittest.main()