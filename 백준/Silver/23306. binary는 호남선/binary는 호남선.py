import sys

def flush():
    sys.stdout.flush()

def main():
    N = int(input())

    print("? 1")
    flush()
    a = int(input())

    print("? {}".format(N))
    flush()
    b = int(input())

    if a == 1 and b == 0:
        print("! -1")
        flush()
    elif a == 0 and b == 1:
        print("! 1")
        flush()
    else:
        print("! 0")
        flush()

if __name__ == "__main__":
    main()
