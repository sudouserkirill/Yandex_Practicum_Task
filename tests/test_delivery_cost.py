import pytest

from delivery_cost import calculate_delivery_cost
from tests.test_data import TestData


@pytest.mark.parametrize("distance, size, fragility, workload, expected", TestData.pairwise_data)
def test_calculate_delivery_cost_pairwise(distance, size, fragility, workload, expected):
    assert calculate_delivery_cost(distance, size, fragility, workload) == expected


@pytest.mark.parametrize("distance, size, fragility, workload", TestData.negative_data)
def test_calculate_delivery_negative(distance, size, fragility, workload):
    try:
        calculate_delivery_cost(distance, size, fragility, workload)
        assert False
    except ValueError as e:
        print(e)
        assert True


@pytest.mark.parametrize("distance, size, fragility, workload, expected", TestData.distance_boundary_values)
def test_calculate_delivery_distance_boundary_values(distance, size, fragility, workload, expected):
    assert calculate_delivery_cost(distance, size, fragility, workload) == expected