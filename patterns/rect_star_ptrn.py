# Print Solid Rectangle Star Pattern
def main():
    n, m = 3, 5

    for i in range(1, n+1):
        for j in range(1, m+1):
            print("*", end=" ")

        print()

if __name__ == "__main__":
    main()