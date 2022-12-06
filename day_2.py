import requests
import json
import urllib.request

strategy_dict = {
    "A X":"4", 
    "A Z":"3",
    "A Y":"8",
    "B X":"1",
    "B Z":"9",
    "B Y":"5",
    "C X":"7",
    "C Y":"2",
    "C Z":"6"
}

def find_total_score(data):
    total_score = 0
    for entry in data:
        total_score += int(strategy_dict[entry])
    return total_score
with open('data.txt', "r") as myfile:
    data = myfile.read().splitlines()
    print(find_total_score(data))
    

