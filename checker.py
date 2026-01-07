class PasswordAnalyzer:
    def __init__(self, dictionary_file=None, 
                 min_length=8, 
                 max_length=64, 
                 require_uppercase=True, 
                 require_lowercase=True, 
                 require_digits=True, 
                 require_symbols=True
                 ):
        """
        Initialize the analyzer.
        Load common passwords if provided.
        """

        #attributes
        self.min_length = min_length
        self.max_length = max_length
        self.require_uppercase = require_uppercase
        self.require_lowercase = require_lowercase
        self.require_digits = require_digits
        self.require_symbols = require_symbols

        #load common passwords
        self.common_passwords = self.load_common_passwords(dictionary_file)

    def load_common_passwords(self, file_path):
        
        """
        Loads a list of common passwords from a file.
        Returns a set for quick lookup.
        """
        try:
            with open("C:\Users\Eric\Downloads\rrockyou\rrockyou.txt", 'r') as f:
                return set(line.strip() for line in f)
        except FileNotFoundError:
            print("Common password file not found.")


        return set()

    def analyze(self, password):
        """
        Main function to analyze a single password.
        Returns a score and feedback.
        """
        score = 0
        feedback = []

        # TODO: call helper methods to evaluate password
        # e.g. score += self.evaluate_length(password)

        return score, feedback

    def evaluate_length(self, password):
        """
        Evaluate length contribution to score.
        """
        if (len(password) >= 8):
            return 10
        elif (len(password) >= 15):
            return 20
        elif (len(password) == 64):
            return 25
        return 0

    def evaluate_char_variety(self, password):
        """
        Evaluate use of uppercase, lowercase, digits, symbols.
        """
        upperNum = 0
        lowerNum = 0
        digitNum = 0
        symbolNum = 0
        for char in password:
            pass
        #still deciding and thinking on how do i implement this properly
        


    def deductions(self, password):
        """
        Deduct points for repeated characters, sequences, keyboard patterns.
        """
        pass

    def check_dictionary(self, password):
        """
        Check if password is a common password (use rockyou wordlist).
        """
        pass

    def generate_feedback(self, password):
        """
        Generate human-readable feedback.
        """
        # TODO: store feedback messages in an array
        pass