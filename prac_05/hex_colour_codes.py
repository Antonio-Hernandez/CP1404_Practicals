COLOURS_TO_HEX = {"aliceblue": "f0f8ff", "aquamarine2": "76eec6", "blanchedalmond": "ffebcd", "blueviolet": "8a2be2",
                  "brown": "a52a2a", "cadetblue": "5f9ea0", "coral": "ff7f50", "cyan": "00ffff", "darkorange": "ff8c00",
                  "deeppink1": "ff1493"}


def main():
    try:
        colour_name = input("Please input the name of the colour \n>> ").lower()
        print("The hex code is #{}".format(COLOURS_TO_HEX[colour_name]))
    except KeyError:
        print("Invalid colour name")

main()
