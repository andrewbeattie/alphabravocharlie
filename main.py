from nato import NatoPractice


if __name__ == "__main__":
    np = NatoPractice()
    while True:
        np.question()
        print(np.score)
        if input("Press Enter to continue") != "":
            break
    np.results()