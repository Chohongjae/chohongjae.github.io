user_input = input().split()
tmp = []
for i in range(int(user_input[0])):
    tmp.append(float(input()))

_max = max(tmp)
_min = min(tmp)

answer = _min
count = 0
while True:
    for i in tmp:
        count += int(i / answer)
    if count == int(user_input[1]):
        break
    else:
        count = 0
        answer -= 0.001

result = round(answer, 2)
if len(str(result)) ==3:
    print(str(result)+'0')
else:
    print(result)
