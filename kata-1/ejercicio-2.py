def print_parsec_to_lightyears(_parsec, _lightyears):
    print("{parsec} parsec, is {lightyears} lightyears"
        .format(
            parsec = str(_parsec), 
            lightyears = str(_lightyears)
            )
        )


if __name__ == "__main__":
    parsec = 11
    lightyears = 3.26156 * parsec
    # Imprimimos la conversion de parsec a años luz
    print_parsec_to_lightyears(parsec, 
                               lightyears)