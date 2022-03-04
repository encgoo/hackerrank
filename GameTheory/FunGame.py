# https://www.hackerrank.com/challenges/fun-game-1/problem?isFullScreen=true

# brute force approach


def fun_game(a, b):
    sz = len(a)
    sum_ = [(0,0,0) for _ in range(sz)]

    for i in range(sz):
        sum_[i] = (a[i] + b[i], a[i], b[i])

    sum_ = sorted(sum_, key=lambda x:x[0], reverse=True)

    p1 = 0
    p2 = 0
    for i in range(sz):
        if i%2 == 0:
            p1 += sum_[i][1]
        else:
            p2 += sum_[i][2]

    if p1 == p2:
        return 'Tie'
    elif p1 > p2:
        return 'First'
    else:
        return 'Second'



if __name__ == '__main__':
    print(fun_game([1,3,4], [5,3,1]))
