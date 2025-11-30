from user_input_validator import UserInputValidator

validator_A = UserInputValidator()
validator_B = UserInputValidator()

sample_data_1 = ["1", "-5", "cat", "0", "42"]
sample_data_2 = ["3.14", "1001", "0", "twelve"]

print("Testing validator A:")
result_A = validator_A.validate_positive_integers(sample_data_1)
print(result_A)  # Should output [1, 42]

print("\nTesting validator B:")
result_B = validator_B.validate_positive_integers(sample_data_2)
print(result_B)  # Should output [1001]