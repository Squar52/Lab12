import math
def surface_area(a, b, h):
    "Площа повної поверхні прямої піраміди з основою-прямокутником a × b і висотою h."
    base = a * b
    slant_a = math.sqrt(h ** 2 + (b / 2) ** 2)
    slant_b = math.sqrt(h ** 2 + (a / 2) ** 2)
    lateral = a * slant_a + b * slant_b
    return base + lateral
def volume(a, b, h):
    """Об'єм прямої піраміди з основою-прямокутником a × b і висотою h."""
    return a * b * h / 3