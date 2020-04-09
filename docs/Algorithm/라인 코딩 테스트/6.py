def solution(directory, command):
    excluded = []
    for cm in command:
        _command = cm.split(' ')[0]
        if _command == 'mkdir':
            directory.append(cm.split(' ')[1])
        elif _command == 'cp':
            for di in directory:
                if di.startswith(cm.split(' ')[1]):
                    directory.append(f"{cm.split(' ')[2]}{di}")
        else:
            for di in directory:
                if di.startswith(cm.split(' ')[1]):
                    excluded.append(di)

    for i in excluded:
        directory.remove(i)
    return sorted(directory)


if __name__ == "__main__":
    print(solution([
"/"
],[
"mkdir /a",
"mkdir /a/b",
"mkdir /a/b/c",
"cp /a/b /",
"rm /a/b/c"
]))
