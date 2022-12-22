import random

PHEONETIC = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
    'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
    'i': 'india', 'j': 'juliett', 'k':  'kilo', 'l': 'lima',
    'm': 'mike', 'n': 'novemeber', 'o': 'oscar', 'p': 'papa',
    'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'viktor', 'w': 'whisky', 'x': 'x-ray',
    'y': 'yankee', 'z': 'zulu', '0': 'ze-ro', '1': 'wun', '2': 'too',
    '3': 'tree', '4': 'fow-er', '5': 'fife', '6': 'six', '7': 'sev-en',
    '8': 'ait', '9': 'nin-er'
}

class String(str):
    def to_nato(self):
        return ' '.join([PHEONETIC[l] for l in self])

class NatoPractice:
    def __init__(self):
        self.score = 0
        self._right = {k: 0 for k in PHEONETIC.keys()}
        self._wrong = {k: 0 for k in PHEONETIC.keys()}

    def question(self):
        question, answer = random.choice(list(PHEONETIC.items()))
        response = input(f'What does {question} correspond to in NATO phonetic?\n')
        if response == answer:
            print("Correct.")
            self.score += 1
            self._right[question] += 1
        else:
            print(f"Incorrect. The answer is {answer}")
            self.score -= 1
            self._wrong[question] += 1

    def results(self):
        total_right = 0
        for v in self._right.values():
            total_right += v

        total_wrong = 0
        for v in self._wrong.values():
            total_wrong += v
        
        print(f"Total Questions: {total_right + total_wrong}")
        print(f"Total Right: {total_right}")
        print(f"Total Wrong {total_wrong}")
        print(f"Percent Accuracy: {round((total_right / (total_right + total_wrong)) * 100, 2)}")
        if input("Display per character stats[y/n]?\n").lower() == 'y':
            for k, r in self._right.items():
                w = self._wrong[k]
                if w + r == 0:
                    continue  
                print(f"For {k}: {r}/{r + w}")
    