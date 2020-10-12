import sys
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


scaler = MinMaxScaler()


def parse_file(file_name):
    file = open(file_name, "r")
    matrice = []
    for line in file:
        (km, price) = line.split(",")
        if km == "km" or price == "price":
            continue
        tab = [int(km), int(price)]
        matrice.append(tab)
    matrice = scaler.fit_transform(matrice)
    x = matrice[:, 0]
    y = matrice[:, 1]
    plt.scatter(x, y)
    return x, y


def model_function(theta_0, theta_1, x):
    estimate_price = theta_0 + (theta_1 * x)
    return estimate_price


def cost_function(old_theta_0, old_theta_1, x, y):
    tmp_t0 = tmp_t1 = 0.0
    for i in range(len(x)):
        tmp_t0 += (old_theta_0 + (old_theta_1 * x[i]) - y[i])
        tmp_t1 += (old_theta_0 + (old_theta_1 * x[i]) - y[i]) * x[i]
    derivative_t0 = (1 / len(x)) * tmp_t0
    derivative_t1 = (1 / len(x)) * tmp_t1
    return derivative_t0, derivative_t1


def gradient_descent(file_name):
    (x, y) = parse_file(file_name)
    theta_0 = theta_1 = 0.0
    learning_rate = 0.035
    for i in range(2000):
        (derivative_t0, derivative_t1) = cost_function(theta_0, theta_1, x, y)
        theta_0 -= derivative_t0 * learning_rate
        theta_1 -= derivative_t1 * learning_rate
    # t0 /= scaler.scale_[0]
    # t1 /= scaler.scale_[1]
    print(theta_0, theta_1)
    plt.plot([theta_0, theta_1], color="pink")
    return theta_0, theta_1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./trainer [data_set]")
    else:
        print("Starting the training")
        (t0, t1) = gradient_descent(sys.argv[1])
        plt.show()
