from game_result import GameResult


class Game:
    def __init__(self) -> None:
        self.question = ""

    def guess(self, guess_num) -> GameResult:
        self.assert_illegal_value(guess_num)
        if self.question == guess_num:
            return GameResult(True, 3, 0)
        else:
            strikes = 0
            balls = 0
            for i in range(len(self.question)):
                if self.question.find(guess_num[i]) == i:
                    strikes += 1
                elif self.question.find(guess_num[i]) != -1:
                    balls += 1
            return GameResult(False, strikes, balls)
    def assert_illegal_value(self, guess_num):
        if guess_num is None:
            raise TypeError()
        if len(guess_num) != 3:
            raise TypeError()
        for num in guess_num:
            if not ord('0') <= ord(num) < ord('9'):
                raise TypeError()
        if self.is_duplicated_number(guess_num):
            raise TypeError()

    def is_duplicated_number(self, guess_num):
        return (guess_num[0] == guess_num[1] or
                guess_num[0] == guess_num[2] or
                guess_num[1] == guess_num[2])
