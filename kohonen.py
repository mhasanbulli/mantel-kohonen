# kohonen.py
import matplotlib.pyplot as plt
import numpy as np


def train(input_data, n_max_iterations, width, height):
    σ0 = max(width, height) / 2  # constant
    α0 = 0.1  # constant
    weights = np.random.random((width, height, 3))  # 10 x 10 grid with 3D indices
    λ = n_max_iterations / np.log(σ0)  # constant
    for t in range(n_max_iterations):
        σt = σ0 * np.exp(-t / λ)  # constant
        αt = α0 * np.exp(-t / λ)  # constant
        for vt in input_data:  # 10 vectors of size 3
            bmu = np.argmin(np.sum((weights - vt) ** 2, axis=2))  # constant
            bmu_x, bmu_y = np.unravel_index(bmu, (width, height))  # constant set
            for x in range(width):
                for y in range(height):
                    di = np.sqrt(((x - bmu_x) ** 2) + ((y - bmu_y) ** 2))  # constant
                    θt = np.exp(-(di**2) / (2 * (σt**2)))  # constant
                    weights[x, y] += αt * θt * (vt - weights[x, y])
    return weights


if __name__ == "__main__":
    # Generate data
    input_data = np.random.random((10, 3))
    image_data = train(input_data, 100, 10, 10)

    plt.imsave("100.png", image_data)

    # Generate data
    input_data = np.random.random((10, 3))
    image_data = train(input_data, 1000, 100, 100)

    plt.imsave("1000.png", image_data)
