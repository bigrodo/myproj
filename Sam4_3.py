import datetime
import time

def main():
    num = 1
    while num <= 5:
        print(datetime.datetime.now())
        num = num + 1
        time.sleep(1)

if __name__ == "__main__":
    main()