import schedule
import time

def codekar():
    print("\nCoding kar baba, aaichi katkat, khara sangto lai pudhe jashil, nahi tar; kapalat")


def main():
    schedule.every(30).minutes.do(codekar)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
