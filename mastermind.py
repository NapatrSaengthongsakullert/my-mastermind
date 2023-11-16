from random import randint


class MastermindGame:
    def __init__(self):
        self.length = 4
        self.answer = [randint(1, 8) for _ in range(4)]
        self.max_rounds = 10

    def start_new_game(self):
        print("Playing Mastermind with 6 colors and 4 positions")
        print(self.answer)
        for i in range(self.max_rounds):
            self.correct = []
            self.used = []
            self.user = input("What is your guess?: ")
            print(f"Your guess is {self.user}")
            for j in range(4):
                if int(self.user[j]) == self.answer[j]:
                    print("*",end='')
                    self.correct.append("*")
                    self.used.append(self.answer[j])
                elif int(self.user[j]) in self.answer:
                    if int(self.user[j]) not in self.used:
                        print("o",end='')
                        self.correct.append("o")
            # MastermindGame.hint()
            # self.check = self.correct.count("*")
            # if self.check == 4:
            #     print(f"You solved it after {i + 1} rounds")
            #     break
            print("\n")

    # def hint(self):
    #     for j in range(4):
    #         if int(self.user[j]) == self.answer[j]:
    #             print("*", end='')
    #             self.correct.append("*")
    #             self.used.append(self.answer[j])
    #         elif int(self.user[j]) in self.answer:
    #             if int(self.user[j]) not in self.used:
    #                 print("o", end='')
    #                 self.correct.append("o")

            self.check = self.correct.count("*")
            if self.check == 4:
                print(f"You solved it after {i + 1} rounds")
                break


if __name__ == "__main__":
    mastermind_game = MastermindGame()
    mastermind_game.start_new_game()
