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
    params = {0: {'mean': [1, -1],
                  'cov': [[2, 0], [0, 2]]},
              1: {'mean': [2, -2],
                  'cov': [[16, 0], [0, 16]]},
              2: {'mean': [3, -3],
                  'cov': [[36, 0], [0, 36]]}
              }
    mixture_idx = np.random.choice(a=3, size=300, replace=True)

    x_cord, y_cord = [], []
    for i in mixture_idx:
        x, y = np.random.multivariate_normal(params[i]['mean'], params[i]['cov'], 1).T
        x_cord.append(x[0])
        y_cord.append(y[0])
    plt_show(x_cord, y_cord, 'Three Gaussians')

    # (d)
    r1, r2, r3 = 1, 0.75, 0.25
    x_cord, y_cord = [], []
    i = 0
    while len(x_cord) < 1000:
        x, y = np.random.uniform(-1, 1, 1), np.random.uniform(-1, 1, 1)
        if ((x**2 < r1**2 - y**2) and (x**2 > r2**2 - y**2)) or (x**2 < r3**2 - y**2):
            x_cord.append(x[0])
            y_cord.append(y[0])
        i += 1

    plt_show(x_cord, y_cord, 'CURE Circles')

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


# suggestion for A
x_cord, y_cord = [], []
i = 0
while len(x_cord) < 300:
    x, y = np.random.uniform(-3, 3, 1), np.random.uniform(-7, 3, 1)
    if ((y > -3*x) and (y < -3*x + 3)) \
            or (((y > 3*x) and (y < 3*x + 3))) \
            or ((y > -5) and (y < -3) and (x > -2) and (x < 2)):
        x_cord.append(x[0])
        y_cord.append(y[0])
    i += 1

plt_show(x_cord, y_cord, 'CURE Circles')
