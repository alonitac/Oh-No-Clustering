import numpy as np
import matplotlib.pyplot as plt

N = 300

# numpy distributions reference https://docs.scipy.org/doc/numpy/reference/routines.random.html


def plt_show(x, y, title):
    plt.plot(x, y, '.')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def sample_AF():
    # sample from F
    x, y = np.random.uniform(0, 7, N//2), np.random.uniform(0, 8, N//2)
    for i, _ in enumerate(x):
        if (5 < x[i]) or ((2 < x[i] < 5) and ((0 < y[i] < 2) or (4 < y[i] < 6))):
            x[i] = 7 - x[i]
            y[i] = 8 - y[i]

    # sample from A
    x_cord, y_cord = [], []
    while len(x_cord) < N/2:
        z, w = np.random.uniform(-3, 3, 1), np.random.uniform(-7, 3, 1)
        if (((w > -3 * z) and (w < -3 * z + 3))
            or ((w > 3 * z) and (w < 3 * z + 3))
            or ((w > -5) and (w < -3) and (z > -2) and (z < 2))) \
            and not (((w > (3 - 3 * z) and w > 3 * z)) or ((w > (3 + 3 * z) and w > -3 * z))):

            x_cord.append(z)
            y_cord.append(w)
    x_cord = [i - 3 for i in x_cord]
    y_cord = [i + 7 for i in y_cord]
    return list(x) + x_cord, list(y)+y_cord


def sample_cure_circles():
    r1, r2, r3 = 1, 0.75, 0.25
    x_cord, y_cord = [], []
    i = 0
    while len(x_cord) < N:
        x, y = np.random.uniform(-1, 1, 1), np.random.uniform(-1, 1, 1)
        if ((x**2 < r1**2 - y**2) and (x**2 > r2**2 - y**2)) or (x**2 < r3**2 - y**2):
            x_cord.append(x[0])
            y_cord.append(y[0])
        i += 1

    return x_cord, y_cord


def sample_three_gaussians():
    params = {0: {'mean': [1, -1],
                  'cov': [[2, 0], [0, 2]]},
              1: {'mean': [2, -2],
                  'cov': [[16, 0], [0, 16]]},
              2: {'mean': [3, -3],
                  'cov': [[36, 0], [0, 36]]}
              }
    mixture_idx = np.random.choice(a=3, size=N, replace=True)

    x_cord, y_cord = [], []
    for i in mixture_idx:
        x, y = np.random.multivariate_normal(params[i]['mean'], params[i]['cov'], 1).T
        x_cord.append(x[0])
        y_cord.append(y[0])

    return x_cord, y_cord


def sample_gaussian():
    x, y = np.random.multivariate_normal([1, 1], [[4, 0], [0, 4]], N).T
    return x, y


def sample_uniform():
    x, y = np.random.uniform(-1, 1, N), np.random.uniform(0, 5, N)
    return x, y


if __name__ == '__main__':
    # (a)
    x, y = sample_uniform()
    plt.figure(figsize=(10, 5))
    plt.suptitle('Uniform distribution, x ∈ [−1, 1], y ∈ [0, 5]')
    plt.subplot(1, 2, 1)
    plt.plot(x, y, '.')

    x, y = sample_uniform()
    plt.subplot(1, 2, 2)
    plt.plot(x, y, '.')
    plt.show()

    # (b)
    x, y = sample_gaussian()
    plt.figure(figsize=(10, 5))
    plt.suptitle('Gaussian with center at [1,1] and std=2')
    plt.subplot(1, 2, 1)
    plt.plot(x, y, '.')

    x, y = sample_gaussian()
    plt.subplot(1, 2, 2)
    plt.plot(x, y, '.')
    plt.show()

    # (c)
    x, y = sample_three_gaussians()
    plt.figure(figsize=(10, 5))
    plt.suptitle('Three Gaussians')
    plt.subplot(1, 2, 1)
    plt.plot(x, y, '.')

    x, y = sample_three_gaussians()
    plt.subplot(1, 2, 2)
    plt.plot(x, y, '.')
    plt.show()

    # (d)
    x, y = sample_cure_circles()
    plt.figure(figsize=(10, 5))
    plt.suptitle('CURE Circles')
    plt.subplot(1, 2, 1)
    plt.plot(x, y, '.')

    x, y = sample_cure_circles()
    plt.subplot(1, 2, 2)
    plt.plot(x, y, '.')
    plt.show()

    # (e)
    x, y = sample_AF()
    plt.figure(figsize=(10, 5))
    plt.suptitle('The first letter of both your first names - AF')
    plt.subplot(1, 2, 1)
    plt.plot(x, y, '.')

    x, y = sample_AF()
    plt.subplot(1, 2, 2)
    plt.plot(x, y, '.')
    plt.show()