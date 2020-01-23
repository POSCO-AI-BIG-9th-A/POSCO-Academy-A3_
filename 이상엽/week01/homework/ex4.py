import os

if not os.path.exists("score.txt"):
    with open("score.txt", "w") as f:
        data = "201901 89 78\n201902 76 84\n201903 67 42\n201904 66 88\n201905 98 99"
        f.write(data)

fIn = open("score.txt", "r")
fOut = open("report.txt", "w")

lines = fIn.readlines()
avg = []
data = ""
for student in lines:
    info = student.split(' ')
    avg = int(info[1])*0.4+int(info[2])*0.6
    data += '%6s %2s %2s %.1f' %(info[0], info[1], info[2].strip(), avg)
    rank = ''
    if avg >= 90:
        rank = 'A'
    elif avg >= 80:
        rank = 'B'
    elif avg >= 70:
        rank = 'C'
    elif avg >= 60:
        rank = 'D'
    else:
        rank = 'F'
    data += '(%s)\n' %(rank)

fOut.write(data)
fIn.close()
fOut.close()
