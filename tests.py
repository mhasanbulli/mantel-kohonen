import numpy as np
from numpy import ndarray
from pytest import fixture

from kohonen import train
from kohonen_refactored import Config
from kohonen_refactored import train as train_refactored


@fixture(scope="session")
def input_data():
    np.random.seed(42)
    return np.random.random((10, 3))


expected = [
    [
        [0.53127524, 0.3007639, 0.32564506],
        [0.45675191, 0.45204877, 0.43943024],
        [0.29678354, 0.37042611, 0.4444905],
    ],
    [
        [0.48217518, 0.36026289, 0.48774274],
        [0.37848495, 0.5149276, 0.43076464],
        [0.38127728, 0.51483262, 0.39687744],
    ],
    [
        [0.48121033, 0.39978173, 0.63485575],
        [0.45083248, 0.59016424, 0.51857288],
        [0.42526711, 0.66460663, 0.3322869],
    ],
]


def test_train_returns_the_same_weights(input_data: ndarray):
    t_weights = train(input_data, 5, 3, 3)
    np.testing.assert_allclose(expected, t_weights)


def test_train_refactored_returns_the_same_weights(input_data: ndarray):
    training_config = Config(n_max_iterations=5, width=3, height=3, learning_rate=0.1)
    weights = np.random.random((training_config.width, training_config.height, 3))

    t_weights = train_refactored(input_data, weights, config=training_config)
    np.testing.assert_allclose(expected, t_weights)
