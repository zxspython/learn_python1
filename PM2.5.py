#PM2.5.py
# 空气质提醒

def main():
    PM=float(input("what is today's PM2.5?\n"))
    #判断PM2.5大小，相应提醒
    if PM > 7.5:
        print("Unhealthy.Be careful")
    if PM < 7.5:
        print("Good.Go runing")
main()
