def calculate_kcal(mass_kg: float, distance_km: float, time_h: float):
    v_kph: float = calculate_velocity(distance_km, time_h)
    vo2_max: float = calculate_vo2_max(v_kph)
    kcal_per_min: float = calculate_kcal_per_min(mass_kg, vo2_max)
    kcal_total: float = calculate_kcal_total(kcal_per_min, time_h)
    return kcal_total


def calculate_velocity(distance_km: float, time_h: float):
    v = distance_km / time_h
    return v


def calculate_vo2_max(v_kph: float):
    vo2_max = 2.209 + (3.1633 * v_kph)
    return vo2_max


def calculate_kcal_per_min(mass_kg: float, vo2_max: float):
    kcal_per_min = 4.86 * mass_kg * vo2_max / 1000
    return kcal_per_min


def calculate_kcal_total(kcal_per_min: float, time_h: float):
    kcal_total = kcal_per_min * (time_h / 60)
    return kcal_total
