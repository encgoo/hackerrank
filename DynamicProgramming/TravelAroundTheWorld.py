#https://www.hackerrank.com/challenges/travel-around-the-world/problem?isFullScreen=true

# we start with a random one (pick the last one for simplicity)
# 1. for the first one, we need to go around the world to check if it can go through.
# 2. We store the good ones
# 3. Once we have good ones, we just need to reach the closest good one, don't need to go around the world
# 4. the last one stored in the stored good one is the closest one.


def go_round(a, b, c, st, n_st):
    n = len(a)
    good = True
    gas = 0
    for i in range(n_st):
        j = (i+st)%n
        gas += a[j]
        gas = min(c, gas)
        if gas >= b[j]:
            gas -= b[j]
        else:
            good = False
            break

    return good


def travelAroundTheWorld(a, b, c):
    sz = len(a)
    assert sz == len(b)

    good_stations = []
    # start with the last one
    idx = sz - 1
    while idx >= 0:
        if good_stations:
            n_st = good_stations[-1] - idx
        else:
            n_st = sz

        ret = go_round(a, b, c, idx, n_st)
        if ret:
            good_stations.append(idx)
        idx -= 1

    return len(good_stations)


if __name__ == '__main__':
    c = 3
    a = [3, 1, 2]
    b = [2, 2, 2]

    print(travelAroundTheWorld(a, b, c))
