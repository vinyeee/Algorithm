import sys

class agent:
    def __init__(self, name,score):
        self.name = name
        self.score = score

agents = []

for _ in range(5):
    name, score = input().split()
    agents.append(agent(name, int(score)))

min_score = sys.maxsize
min_name = ""

for i in range(5):
    if agents[i].score < min_score:
        min_score = agents[i].score
        min_name = agents[i].name


print(min_name, min_score)

    