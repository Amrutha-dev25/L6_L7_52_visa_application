import math


def parse_application(text):
    try:
        if not isinstance(text, str) or text.count(':') != 1:
            return "", 0

        visa, entries = text.split(':')
        visa = visa.strip()
        entries = int(entries.strip())

        if not visa or entries <= 0:
            return "", 0

        return visa.title(), entries

    except (ValueError, TypeError):
        return "", 0


def processing_average(days_csv):
    try:
        if not isinstance(days_csv, str) or not days_csv.strip():
            return 0

        values = [int(x.strip()) for x in days_csv.split(',')]

        if not values or any(x < 0 for x in values):
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return 0


def payable_fee(text):
    try:
        if not isinstance(text, str) or text.count('|') != 1:
            return 0.0

        fee, discount = text.split('|')

        fee = float(fee.strip())
        discount = float(discount.strip())

        if not math.isfinite(fee) or not math.isfinite(discount):
            return 0.0

        if fee < 0 or discount < 0:
            return 0.0

        total = fee * 1.18 - discount
        return max(total, 0.0)

    except (ValueError, TypeError):
        return 0.0


def main():
    print("==== Running parse_application ====")
    user_input = input("Enter visa type:entries (e.g. tourist:2): ")
    result = parse_application(user_input)
    print("Visa Type and Entries:", result)

    print("\n==== Running processing_average ====")
    user_input = input("Enter processing days as CSV (e.g. 5,10,21): ")
    result = processing_average(user_input)
    print("Average Processing Days:", result)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 6000|500): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result)


if __name__ == "__main__":
    main()