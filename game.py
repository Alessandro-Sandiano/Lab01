import random
import Player

class Question:
    def __init__(self, text="", level="", correct="", options=[]):
        self._text = text
        self._level = level
        self._correct = correct
        self._options = options

    @staticmethod
    def load_questions(file_name):
        """
        Load the file of questions and put them in a list.
        :param file_name: name of the file to load.
        :return: list of Question objects.
        """
        questions_list = []
        with open(f"{file_name}.txt", encoding="utf-8") as file:
            while True:
                questions_list.append(Question(file.readline().strip(), file.readline().strip(), file.readline().strip(),
                                            [file.readline().strip(), file.readline().strip(),
                                             file.readline().strip()]))
                if file.readline() == "": break
        return questions_list

    @staticmethod
    def play(questions_list):
        """
        Manage game mechanics.
        :param questions_list: list of Question objects.
        :return: Player object.
        """
        print("Benvenuto a Trivia Game! Digitare la risposta corretta o il numero ad essa corrispondente.\n")
        player = Player.Player()
        c = True

        while c is True:

            questions_by_level = [l for l in questions_list if int(l.level) == player.score]
            if len(questions_by_level) == 0: break

            random_question = questions_by_level[random.randint(0, len(questions_by_level) - 1)]
            random_question.options.append(random_question.correct)
            random.shuffle(random_question.options)

            print("\nLivello " + str(player.score) + ") " + random_question.text)
            for r in random_question.options:
                print(f"{random_question.options.index(r) + 1}. {r}")
            print("\nInserisci la risposta: ", end="")

            while True:
                answer = input()
                if answer == "":
                    print("Non è stata inserita alcuna risposta. Riprovare: ", end="")
                    continue
                try:
                    if int(answer) in range(1, len(random_question.options) + 1):
                        if random_question.options[int(answer) - 1] == random_question.correct:
                            print("Risposta corretta!")
                            player.score += 1
                        else:
                            print(
                                f"Risposta sbagliata! La risposta corretta era: {random_question.options.index(random_question.correct) + 1}")
                            c = False
                        break
                    print("Il numero inserito non è associato ad alcuna risposta. Riprovare: ", end="")
                except:
                    if answer in random_question.options:
                        if answer == random_question.correct:
                            print("Risposta corretta!")
                            player.score += 1
                        else:
                            print(
                                f"Risposta sbagliata! La risposta corretta era: {random_question.options.index(random_question.correct) + 1}")
                            c = False
                        break
                    print("La risposta non è stata digitata correttamente. Riprovare: ", end="")

        print("\nHai totalizzato " + str(player.score) + " punti!")
        player.name = input("Inserisci il tuo nickname: ")
        return player

    @property
    def text(self):
        return self._text

    @property
    def level(self):
        return self._level

    @property
    def correct(self):
        return self._correct

    @property
    def options(self):
        return self._options
