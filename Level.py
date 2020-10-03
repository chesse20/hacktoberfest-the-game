def main():
    print("Please only call functions from this module");
    return None


def Level(int exp):
    int Level = math.round(log10(exp)/100);
    return Level;

if __name__ == "__main__":
    main()
