if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name, score])

    scores = sorted(set([score for name, score in a]))
    second_lowest = scores[1]

    names_with_second_lowest = [name for name, score in a if score == second_lowest]
    for name in sorted(names_with_second_lowest):
        print(name)
