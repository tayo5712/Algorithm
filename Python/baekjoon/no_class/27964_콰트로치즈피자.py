n = int(input())
lst = list(input().split())
cheese_set = set()
for i in range(n):
  if lst[i].endswith("Cheese"):
    cheese_set.add(lst[i])
if len(cheese_set) >= 4:
  print("yummy")
else:
  print("sad")
