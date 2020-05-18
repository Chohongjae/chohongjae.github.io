def solution(k, room_number):
    charged_room = {}

    for i in room_number:
        tmp = []
        try:
            if charged_room[i]:
                empty_rooom = charged_room[i]
                tmp.append(i)
                while True:
                    try:
                        if charged_room[empty_rooom]:  # charged_room[empty_rooom] 안비어있따.
                            tmp.append(empty_rooom)
                            empty_rooom = charged_room[empty_rooom]
                    except:
                        charged_room[empty_rooom] = empty_rooom + 1
                        break

                for j in tmp:
                    charged_room[j] = empty_rooom + 1

        except:
            charged_room[i] = i + 1

    return list(charged_room.keys())


if __name__ == '__main__':
    print(solution(10, [1, 3, 4, 1, 3, 1]))
{1: 2}
{1: 2, 3: 4}
{1: 2, 3: 4, 4: 5}
