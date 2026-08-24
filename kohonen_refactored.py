from typing import Annotated

import numpy as np
from numpy import ndarray
from pydantic import BaseModel, Field


class Config(BaseModel):
    n_max_iterations: Annotated[int, Field(gt=0)]
    width: Annotated[int, Field(gt=2)]
    height: Annotated[int, Field(gt=2)]
    learning_rate: float = 0.1


def update_weights(
    w: ndarray,
    d: ndarray,
    grid_x: ndarray,
    grid_y: ndarray,
    bmu_x: np.integer,
    bmu_y: np.integer,
    radius_decay: float,
    learning_rate_decay: float,
) -> None:
    grid_distance = np.sqrt(((grid_x - bmu_x) ** 2) + ((grid_y - bmu_y) ** 2))
    influence = np.exp(-(grid_distance**2) / (2 * (radius_decay**2)))
    w += learning_rate_decay * influence[..., np.newaxis] * (d - w)


def train(input_data: ndarray, weights: ndarray, config: Config) -> ndarray:
    if input_data.shape[-1] != weights.shape[-1]:
        raise ValueError(
            f"input_data feature dim ({input_data.shape[-1]}) must match weights feature dim ({weights.shape[-1]})"
        )

    neighbour_radius = max(config.width, config.height) / 2
    radius_decay_const = config.n_max_iterations / np.log(neighbour_radius)

    radius_decay = [neighbour_radius * np.exp(-t / radius_decay_const) for t in range(config.n_max_iterations)]
    learning_rate_decay = [
        config.learning_rate * np.exp(-t / radius_decay_const) for t in range(config.n_max_iterations)
    ]

    grid_x, grid_y = np.indices((config.width, config.height))

    for i in range(config.n_max_iterations):
        for d in input_data:
            bmu = np.argmin(np.sum((weights - d) ** 2, axis=2))
            bmu_x, bmu_y = np.unravel_index(bmu, (config.width, config.height))

            update_weights(
                w=weights,
                d=d,
                grid_x=grid_x,
                grid_y=grid_y,
                bmu_x=bmu_x,
                bmu_y=bmu_y,
                radius_decay=radius_decay[i],
                learning_rate_decay=learning_rate_decay[i],
            )

    return weights
