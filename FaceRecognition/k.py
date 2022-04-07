from datetime import datetime
def markAttendance(name):
    with open('Report.csv', 'r+') as f:
        myDataList = f.readlines()

        nameList = []
        for line in myDataList:

            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString1 = now.strftime('%d:%m:%y')
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString1},{dtString}')
                break
