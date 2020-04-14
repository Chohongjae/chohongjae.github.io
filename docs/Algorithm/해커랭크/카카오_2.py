def requestsServed(timestamp, top):
    timestamp.sort()

    result = 0
    tmp = 0
    for i in top:
        for idx, j in enumerate(timestamp):
            if j > i:
                timestamp = timestamp[idx:]

                print('#', j, timestamp)
                result += tmp
                tmp = 0
                break
            else:
                tmp += 1
                timestamp = timestamp[idx:]
                print('@', j, timestamp)
                if tmp % 5 == 0:
                    result += tmp
                    tmp = 0
                    break

    return result


if __name__ == "__main__":

    timestamp_count = int(input().strip())

    timestamp = []

    for _ in range(timestamp_count):
        timestamp_item = int(input().strip())
        timestamp.append(timestamp_item)

    top_count = int(input().strip())

    top = []

    for _ in range(top_count):
        top_item = int(input().strip())
        top.append(top_item)

    result = requestsServed(timestamp, top)
    print(result)
