from my_parser import my_parser


def main():
    crypto = input("Hello, please, enter a crypto name on stock market (for example, ETHUSD):\n")
    try:
        crypto = crypto.upper()
    except:
        print("Incorrect input. Try again.")

    my_parser(crypto)


if __name__ == '__main__':
    main()
