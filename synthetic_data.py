import numpy as np
import matplotlib.pyplot as plt

N = 1000

# numpy distributions reference https://docs.scipy.org/doc/numpy/reference/routines.random.html


def plt_show(x, y, title):
    plt.plot(x, y, '.')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    # (a)
    x, y = np.random.uniform(-1, 1, N), np.random.uniform(0, 5, N)
    plt_show(x, y, 'Uniform distribution, x ∈ [−1, 1], y ∈ [0, 5]')

    # (b)
    x, y = np.random.multivariate_normal([1, 1], [[4, 0], [0, 4]], N).T
    plt_show(x, y, 'Gaussian with center at [1,1] and std=2')

    # (c)
    # to be implemented

    # (d)
    # to be implemented

    # (e)
    # sample from F
    x, y = np.random.uniform(0, 7, N), np.random.uniform(0, 8, N)
    for i, _ in enumerate(x):
        if (5 < x[i]) or ((2 < x[i] < 5) and ((0 < y[i] < 2) or (4 < y[i] < 6))):
            x[i] = 7 - x[i]
            y[i] = 8 - y[i]

    # sample from A
    # z, w = np.random.uniform(0, 7, N), np.random.uniform(0, 8, N)
    # for i, _ in enumerate(x):
    #     if (5 < x[i]) or ((2 < x[i] < 5) and ((0 < y[i] < 2) or (4 < y[i] < 6))):
    #         x[i] = 7 - x[i]
    #         y[i] = 8 - y[i]
    plt_show(x, y, 'The first letter of both your first names - AF')





