import sys
from sklearn.preprocessing import MinMaxScaler


def parse_file(file_name):
    file = open(file_name, "r")
    matrice = []
    for line in file:
        (km, price) = line.split(",")
        if km == "km" or price == "price":
            continue
        tab = [int(km), int(price)]
        matrice.append(tab)
    matrice = MinMaxScaler().fit_transform(matrice)
    x = matrice[:, 0]
    y = matrice[:, 1]
    return x, y


def model_function(theta_0, theta_1, x):
    estimate_price = (theta_0 + (theta_1 * x))
    return estimate_price


def cost_function(old_theta_0, old_theta_1, x, y):
    tmp_t0 = tmp_t1 = 0.0
    for i in range(len(x)):
        tmp_t0 += (model_function(old_theta_0, old_theta_1, x[i]) - y[i])
        tmp_t1 += ((model_function(old_theta_0, old_theta_1, x[i]) - y[i]) * x[i])
    derivative_t0 = (1 / len(x)) * tmp_t0
    derivative_t1 = (1 / len(y)) * tmp_t1
    return derivative_t0, derivative_t1


def gradient_descent(file_name):
    (x, y) = parse_file(file_name)
    t0 = t1 = 0.0
    ratio = 0.001
    for i in range(1000):
        (derivative_t0, derivative_t1) = cost_function(t0, t1, x, y)
        t0 -= ratio * derivative_t0
        t1 -= ratio * derivative_t1
    return t0, t1


# def export_theta(final_t0, final_t1):
#     print(final_t0, final_t1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./trainer [data_set]")
    else:
        print("Starting the training")
        (t0, t1) = gradient_descent(sys.argv[1])
        print(t0, t1)
        val = input("Get km ")
        test = model_function(t0, t1, float(val))
        print(test)
        # export_theta(t0, t1)
