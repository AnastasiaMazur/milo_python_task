import sys

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_IN_MONTH_LEAP = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def transform_year(year):
    return "200{}".format(year) if len(year) == 1 else "20{}".format(year)


def is_leap_year(year):
    return True if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 else False


def is_valid_date(year, month, day):
    if not 1 <= month <= 12 or not 2000 <= year <= 2999 or not 1 <= day <= 31:
        return False

    if is_leap_year(year):
        if day > DAYS_IN_MONTH_LEAP[month - 1]:
            return False
    else:
        if day > DAYS_IN_MONTH[month - 1]:
            return False

    return True


def get_list_posible_variants(input_data):
    posible_years = []

    # if in input data has four digits this is year
    [posible_years.append(value) for value in input_data if len(value) == 4]

    # if in input data doesnt has four digits, possible years is first or last digits
    if not len(posible_years):
        posible_years.append(input_data[0])
        posible_years.append(input_data[2])

    list_posibile_variants = []
    for posible_year in posible_years:
        if len(posible_year) == 4:
            year = posible_year
        else:
            year = transform_year(posible_year)

        data = input_data.copy()
        data.remove(posible_year)

        if int(data[0]) > 12:
            list_posibile_variants.append((int(year), int(data[1]), int(data[0])))
        elif int(data[1]) > 12:
            list_posibile_variants.append((int(year), int(data[0]), int(data[1])))
        else:
            list_posibile_variants.append((int(year), int(data[0]), int(data[1])))
            list_posibile_variants.append((int(year), int(data[1]), int(data[0])))

    return list_posibile_variants


def convert(input_string):
    input_data = input_string.split("/")
    list_posibile_variants = sorted(get_list_posible_variants(input_data))
    for date in list_posibile_variants:
        year, month, day = date
        if is_valid_date(year, month, day):
            return "{}-{:02}-{:02}".format(year, month, day)
    return "{} is illegal".format(input_string)


if __name__ == '__main__':
    input_string = sys.argv[1]
    print(convert(input_string))
