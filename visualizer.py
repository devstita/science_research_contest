import matplotlib.pyplot as plt


def visualize(x, x_label, y, y_label):
    plt.scatter(x, y, label='Title')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.show()
