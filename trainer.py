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


def cost_function(theta_0, theta_1, x, y):
    tmp_t0 = tmp_t1 = 0.0
    for i in range(len(x)):
        tmp_t0 += ((theta_0 + (theta_1 * x[i])) - y[i])
        tmp_t1 += ((theta_0 + (theta_1 * x[i])) - y[i]) * x[i]
    derivative_t0 = (1 / len(x)) * tmp_t0
    derivative_t1 = (1 / len(x)) * tmp_t1
    return derivative_t0, derivative_t1


def gradient_descent(file_name):
    (x, y) = parse_file(file_name)
    theta_0 = theta_1 = 0.0
    learning_rate = 0.5
    for i in range(1000):
        (derivative_t0, derivative_t1) = cost_function(theta_0, theta_1, x, y)
        theta_0 -= learning_rate * derivative_t0
        theta_1 -= learning_rate * derivative_t1
    print(theta_0, theta_1)
    plt.plot([theta_0, theta_1], color="red")
    return theta_0, theta_1


def export_theta(theta_0, theta_1):
    file = open("theta.csv", "w")
    file.write("{t0},{t1}\n".format(t0=theta_0, t1=theta_1))
    file.close()
    plt.show()
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./trainer [data_set]")
    else:
        print("Starting the training")
        (t0, t1) = gradient_descent(sys.argv[1])
        export_theta(t0, t1)
