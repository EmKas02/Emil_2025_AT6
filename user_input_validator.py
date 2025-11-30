class UserInputValidator:

    def validate_positive_integers(self, input_list):
       
        valid_integers = []
        for item in input_list:
            # We check if it's a digit (no negative signs, no decimals) and greater than 0.
            if item.isdigit():
                number = int(item)
                if number > 0:
                    valid_integers.append(number)
        self._display_validation_message()
        return valid_integers

    def _display_validation_message(self):
        print("Validation done! Here's your list of positive integers.")
        