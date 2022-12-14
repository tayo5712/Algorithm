problem = input()
if problem.find("()") != -1:
    print("ROCK")
else:   # eval 만세
    try:
        eval(problem.replace("/", "&").replace("*", "&").replace("+", "&").replace("-", "&"))   # +3 이런거 출력안되게
        try:
            print(eval(problem.replace("/", "//"))) # 소수점 안나오게 
        except:
            print("ROCK")
    except:
        print("ROCK")