# main.py

from demographic_data_analyzer import calculate_demographic_data
import unittest
import test_module

# Run the function and print results
calculate_demographic_data()

# Run the unit tests
print("\nRunning unit tests...\n")
unittest.main(module=test_module, exit=False)
