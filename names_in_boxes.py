__author__ = 'dwintz'

import numpy as np


def play_the_game(people=10, tries=.5):
    tries = round(people*tries)
    success = people*[False]

    inside = np.random.permutation(people)
    outside = np.random.permutation(people)
    inside_boxes = {}
    outside_boxes = {}
    for i in range(people):
        inside_boxes[i] = inside[i]
        outside_boxes[i] = outside[i]

    for person in range(people):
        spot = outside_boxes[person]
        for attempt in range(tries):
            if inside_boxes[spot] == person:
                success[person] = True
                break
            else:
                spot = outside_boxes[inside_boxes[spot]]

    return True if success.count(True) == len(success) else False

if __name__ == '__main__':

    count = 0
    iter = 1000
    for i in range(iter):
        if play_the_game(100):
            count += 1
    print(count/iter)