def loadData():
    measurements = []
    with open('data.txt', 'r') as f:
        for line in f:
            measurements.append(line.replace('\n', '').split('x'))
    return measurements


if __name__ == '__main__':
    measurements = loadData()

    # Part 1
    sum = 0
    for data in measurements:
        lxh = int(data[0]) * int(data[1])
        lxw = int(data[0]) * int(data[2])
        wxh = int(data[1]) * int(data[2])

        wrap = lxh * 2 + lxw * 2 + wxh * 2 + min([lxw, lxh, wxh])
        sum = sum + wrap
    print(f'P1 {sum}')

    # Part 2
    sum = 0
    for data in measurements:
        lwh = [int(data[0]), int(data[1]), int(data[2])]
        lwh.sort()
        sum = sum + lwh[0] * 2 + lwh[1] * 2 + lwh[0] * lwh[1] * lwh[2]
    print(f'P2 {sum}')