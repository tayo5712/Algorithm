from datetime import datetime

HH, MM = map(int, input().split())
start = datetime(year=2022, month=1, day=1, hour=9)
end = datetime(year=2022, month=1, day=1, hour=HH, minute=MM)
print(((end-start)//60).seconds)