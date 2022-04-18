import twl

import argparse
parser = argparse.ArgumentParser(description="WordleSolver")
parser.add_argument("starting_word", type=str, help="First word the solver will try to use")
args = parser.parse_args()


def get_english_word_of_length(length: int):
    english_words_of_length = []
    words = set(twl.iterator())
    for word in words:
        if len(word) != length:
            continue

        english_words_of_length.append(word)

    return english_words_of_length


class Letter:
    def __init__(self, letter, *, is_in_word=False, is_in_correct_place=False):
        self.letter = letter

        self.is_in_correct_place = is_in_correct_place #a green letter
        if self.is_in_correct_place:
            self.is_in_word = True #if letter is green it is also yellow
        else:
            self.is_in_word = is_in_word #a yellow letter


    def __str__(self):
        return self.letter


    @classmethod
    def from_response(cls, response, *, letter):
        if response == "g":
            return cls(letter, is_in_correct_place=True)

        elif response == "y":
            return cls(letter, is_in_word=True)

        elif response == "n":
            return cls(letter)

        else:
            raise ValueError("Invalid response")


class Solver:
    def __init__(self, starting_word: str):
        self.solving = True
        self.possible_words = get_english_word_of_length(5)
        self.grey_letters = []
        self.yellow_letters = {}
        self.green_letters = {}
        self.try_word(starting_word)


    def try_word(self, word):
        self.possible_words.remove(word)
        print(f"Guess: {word}")

        responses = {}

        for letter in word:
            result = input(f"Letter {letter} is: (y/g/n) ")
            responses[letter] = result

        self.try_word(self.process_result(responses, guess_word=word))


    def add_new_letters(self, responses: dict, *, guess_word):
        for let, response in responses.items():
            letter = Letter.from_response(response, letter=let)

            if not letter.is_in_word:
                self.grey_letters.append(str(letter))

            if letter.is_in_word and not letter.is_in_correct_place:
                self.yellow_letters[str(letter)] = list(guess_word).index(str(letter))

            if letter.is_in_correct_place:
                self.green_letters[str(letter)] = list(guess_word).index(str(letter))


    def process_result(self, responses: dict, *, guess_word):
        self.add_new_letters(responses, guess_word=guess_word)

        if len(self.green_letters) == 5:
            print(f"Winning word: {guess_word}")
            exit()

        for word in self.possible_words:
            correct = True
            number_of_correct_letters = 0

            for letter in self.grey_letters:
                if letter in list(word):
                    correct = False

            for letter, index in self.yellow_letters.items():
                if not letter in list(word):
                    correct = False

                elif list(word).index(str(letter)) == index:
                    correct = False

            for letter, index in self.green_letters.items():
                if not letter in list(word):
                    correct = False

                elif list(word).index(str(letter)) != index:
                    correct = False

            if correct:
                return word


if __name__ == "__main__":
    solver = Solver(args.starting_word)
