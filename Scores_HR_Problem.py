if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

    # Find min score
    min_score = min(scores, key=lambda x: x[1])

    # Keep only students with score higher than min
    scores = [score for score in scores if score[1] > min_score[1]]
    print(scores)
    new_scores = []
    for x in scores:
        if score > min_score:
            new_scores.append(x)



