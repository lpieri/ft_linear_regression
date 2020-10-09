import sys


def calc_estimate_price(tmp_t0, tmp_t1, km, price):
    estimate_price = (tmp_t0 + (tmp_t1 * km)) - price
    return estimate_price


def trainer(file_name):
    file = open(file_name, "r")
    t0 = t1 = new_t0 = new_t1 = 0.0
    ratio = 0.5
    for line in file:
        (km, price) = line.split(",")
        if km == "km":
            continue
        price = int(price)
        km = int(km)
        print(km, price)
        new_t0 = ratio * calc_estimate_price(t0, t1, km, price)
        new_t1 = ratio * (calc_estimate_price(t0, t1, km, price) * km)
        t0 = new_t0
        t1 = new_t1
        print(t0, t1)
    return t0, t1


def export_theta(final_t0, final_t1):
    print(final_t0, final_t1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./trainer [data_set]")
    else:
        print("Starting the training")
        (t0, t1) = trainer(sys.argv[1])
        export_theta(t0, t1)
