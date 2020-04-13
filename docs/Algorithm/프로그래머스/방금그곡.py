def chage_sharp(m):
    stack = []
    for idx, i in enumerate(m):
        if i == '#':
            stack.append(stack.pop().lower())
        else:
            stack.append(i)

    return ''.join(stack)


def solution(m, musicinfos):
    m = chage_sharp(m)
    result = []
    for idx, music_info in enumerate(musicinfos):
        _music_info = music_info.split(',')
        name = _music_info[2]
        sheet = chage_sharp(_music_info[3])

        start_time = int(_music_info[0].split(':')[0]) * 60 + int(_music_info[0].split(':')[1])
        end_time = int(_music_info[1].split(':')[0]) * 60 + int(_music_info[1].split(':')[1])
        play_time = end_time - start_time

        if len(sheet) < play_time:
            sheet = int((play_time / len(sheet))) * sheet + sheet[:int((play_time % len(sheet)))]
        elif len(sheet) > play_time:
            sheet = sheet[:play_time]

        if m in sheet:
            result.append((name, play_time, idx))

    if len(result) >= 2:
        return sorted(result, key=lambda x: (-x[1], x[2]))[0][0]
    elif len(result) == 1:
        return result[0][0]
    else:
        return '(None)'


if __name__ == "__main__":
    print(solution('CC', ["04:00,04:02,ZERO,#BCC", "15:00,15:02,FIRST,#BCC", "04:00,04:02,SECOND,#BCC",
                          "04:00,04:03,THIRD,#BCC"]))
