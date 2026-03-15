import operator

class Player:
    def __init__(self):
        self._name = ""
        self._score = 0

    def load_players(self, file_name):
        """
        Load the file of players and put them in a list with their own score, including the current player.
        :param file_name: name of the file to load.
        :return: list of Player objects.
        """
        scores = [f"{self._name} {self._score}\n"]
        with open(f"{file_name}.txt", encoding="utf-8") as file:
            '''
            while True:
                scores.append(file.readline())
                if scores[len(scores)-1]=="":
                    scores.pop(len(scores)-1)
                    break
            '''
            scores.extend(file.readlines())
        return scores

    @staticmethod
    def sort_by_score(scores):
        """
        Sort the players by their scores.
        :param scores: list of Player objects.
        :return: list of Player objects sorted by score.
        """

        '''
        scores.sort(key=operator.itemgetter(0))
        scores.sort(key=operator.itemgetter(-2), reverse=True)
        '''
        scores.sort(key=lambda p: (-ord(p[-2]), p[0]))
        return scores

    @staticmethod
    def update_players(file_name, scores):
        """
        Write the updated players list to a file.
        :param file_name: name of the file to write.
        :param scores: list of Player objects.
        :return: None
        """
        with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
            for p in scores:
                file.write(p)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
