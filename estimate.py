import sys
from sklearn.preprocessing import MinMaxScaler


def calc_price(theta_0, theta_1, kilometer):
    est_price = theta_0 + kilometer * theta_1
    return est_price


def get_scale():
    f = open("data.csv", "r")
    matrice = []
    scaler = MinMaxScaler()
    for line in f:
        (km, price) = line.split(",")
        if km == "km" or price == "price":
            continue
        tab = [int(km), int(price)]
        matrice.append(tab)
    scaler.fit(matrice)
    return scaler


def get_theta():
    file = open("theta.csv", "r")
    line = file.read()
    (t_0, t_1) = line.split(",")
    return float(t_0), float(t_1)


def get_kilometer():
    if len(sys.argv) < 2:
        print("Please enter kilometer here:")
        kilometer = input("> ")
    else:
        if sys.argv[1] == "-h":
            print("Usage: estimate.py [kilometer or in stdin]")
        else:
            kilometer = sys.argv[1]
    if not kilometer.isdigit():
        print("[ERROR]: The entered kilometers are not digital.")
        exit(-1)
    return int(kilometer)


if __name__ == '__main__':
    kilometer = get_kilometer()
    scaler = get_scale()
    (theta_0, theta_1) = get_theta()
    kilometer_scale = scaler.transform([[kilometer, 0]])[0][0]
    price_scale = calc_price(theta_0, theta_1, kilometer_scale)
    price = scaler.inverse_transform([[0, price_scale]])[0][1]
    print("The estimated price is:", int(price))
