def segment(x, arr):
    start = 0
    max_of_min = 0

    if x == 1:
        return max(arr)
    else:
        for pivot in range(x, len(arr) + 1):
            tmp_min = min(arr[start:pivot])
            if max_of_min < tmp_min:
                max_of_min = tmp_min
            start += 1

        return max_of_min


if __name__ == "__main__":
    print(segment(3, [7, 8, 11, 3, 2, 1, 17, 55]))
