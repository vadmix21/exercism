EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Вычисляет оставшееся время выпекания."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Вычисляет время на подготовку всех слоев лазаньи."""
    return number_of_layers * PREPARATION_TIME_PER_LAYER

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Вычисляет общее время, затраченное на приготовление к этому моменту."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time