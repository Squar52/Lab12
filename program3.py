import pyramid
a = float(input("Введіть сторону основи a: "))
b = float(input("Введіть сторону основи b: "))
h = float(input("Введіть висоту піраміди h: "))
print("Площа поверхні:", round(pyramid.surface_area(a, b, h), 2))
print("Об'єм:", round(pyramid.volume(a, b, h), 2))