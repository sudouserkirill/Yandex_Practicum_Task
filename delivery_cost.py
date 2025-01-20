def calculate_delivery_cost(delivery_distance: int,
                            cargo_size: str,
                            cargo_fragility: bool,
                            delivery_workload: float) -> float:
    """Функция расчета стоимости доставки"""

    base_cost = 0

    # Проверяем параметр "Расстояния до пункта назначения"
    if type(delivery_distance) != int:
        raise ValueError((f"Передано некорректное значение расстояния до пункта назначения: {delivery_distance}."
                         f" Оно может быть только числового типа."))
    if delivery_distance <= 0:
        raise ValueError(f"Передано некорректное значение расстояния до пункта назначения: {delivery_distance}."
                         f" Оно не может быть отрицательным числом или равным 0.")
    if delivery_distance <= 2:
        base_cost += 50
    elif delivery_distance <= 10:
        base_cost += 100
    elif delivery_distance <= 30:
        base_cost += 200
    else:
        base_cost += 300

    # Проверяем параметр "Габариты груза"
    if type(cargo_size) != str:
        raise ValueError((f"Передано некорректное значение размера груза: {cargo_size}."
                         f" Оно может быть только строкового типа."))
    if cargo_size == 'large':
        base_cost += 200
    elif cargo_size == 'small':
        base_cost += 100
    else:
        raise ValueError(f"Передано некорректное значение размера груза: {cargo_size}."
                         f" Оно может быть либо 'large', либо 'small'")

    # Проверяем параметр "Хрупкость"
    if type(cargo_fragility) != bool:
        raise ValueError((f"Передано некорректное значение хрупкости: {cargo_fragility}."
                         f" Оно может быть только логического типа."))
    if cargo_fragility:
        if delivery_distance > 30:
            raise ValueError("Хрупкие грузы нельзя возить на расстояние более 30 км.")
        base_cost += 300

    # Проверяем параметр "Загрузку доставки"
    if type(delivery_workload) != str:
        raise ValueError((f"Передано некорректное значение размера груза: {delivery_workload}."
                         f" Оно может быть только строкового типа."))
    if delivery_workload == 'very high':
        workload_coefficient = 1.6
    elif delivery_workload == 'high':
        workload_coefficient = 1.4
    elif delivery_workload == 'increased':
        workload_coefficient = 1.2
    else:
        workload_coefficient = 1

    total_cost = base_cost * workload_coefficient

    return max(400.0, total_cost)
