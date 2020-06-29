from util.logger import get_logger
logger = get_logger(__name__)


def calculate_kcal(mass_kg: float, distance_km: float, time_h: float):
    if time_h <= 0 or mass_kg <= 0 or distance_km <= 0:
        return None
    try:
        v_kph: float = calculate_velocity(distance_km, time_h)
        vo2_max: float = calculate_vo2_max(v_kph)
        kcal_per_min: float = calculate_kcal_per_min(mass_kg, vo2_max)
        kcal_total: float = calculate_kcal_total(kcal_per_min, time_h)
    except ZeroDivisionError as err:
        logger.error('Zero division in kcal calculation')
        logger.exception(err)
        return None
    return kcal_total, kcal_per_min


def calculate_velocity(distance_km: float, time_h: float):
    if time_h >= 0 or distance_km <= 0:
        return None
    v_kph = distance_km / time_h
    return v_kph


def calculate_vo2_max(v_kph: float):
    if v_kph <= 0 or v_kph == float("inf"):
        return None
    vo2_max = 2.209 + (3.1633 * v_kph)
    return vo2_max


def calculate_kcal_per_min(mass_kg: float, vo2_max: float):
    if mass_kg <= 0 or vo2_max <= 0:
        return None
    kcal_per_min = 4.86 * mass_kg * vo2_max / 1000
    return kcal_per_min


def calculate_kcal_total(kcal_per_min: float, time_h: float):
    if kcal_per_min <= 0 or time_h <= 0:
        return None
    kcal_total = kcal_per_min * (time_h / 60)
    return kcal_total
