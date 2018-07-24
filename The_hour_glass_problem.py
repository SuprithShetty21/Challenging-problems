#refer the readme for the details
def calculator(arr):
    tl = tm = tr = mm = bl = bm = br = 0; smax = -100*10;
    for r in range(len(arr) - 2):
        for c in range(len(arr[r]) - 2):
            tl = arr[r][c]
            tm = arr[r][c + 1]
            tr = arr[r][c + 2]
            mm = arr[r + 1][c + 1]
            bl = arr[r + 2][c]
            bm = arr[r + 2][c + 1]
            br = arr[r + 2][c + 2]
            summ = tl + tm + tr + mm + bl + bm + br
            smax = max(smax, summ)
    return smax

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    smax = calculator(arr)
    print(smax)
