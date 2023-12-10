from datetime import datetime, timedelta

d = datetime.now()
cd = datetime.now()
td = timedelta(hours=1)
for i in range(24 * 7):
    # if d.weekday() == 6:
    #     break
    cd = cd + td
print(d, cd, sep="\n")
print(i)
