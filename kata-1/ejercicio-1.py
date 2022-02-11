from datetime import date

def print_today():
    print("Today's date is: {}"
        .format(
            str(date.today())
            )
        )

if __name__ == "__main__":
    # Imprimimos la fecha del dia de hoy
    print_today()