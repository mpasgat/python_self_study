import math as m

def area(shape: dict) -> str:
    match shape:
        case {'type': 'circle', 'radius': r}:
            return f'Area of circle with radius {r} is {m.pi * r ** 2}'
        case {'type': 'rectangle', 'width': w, 'height': h}:
            return f'Area of rectangle with sides {w} and {h} is {w * h}'
        case {'type': 'triangle', 'sides': [a, b, c]}:
            p = (a + b + c) / 2
            return f'Area of triangle with sides {a}, {b}, and {c} is {m.sqrt(p * (p - a) * (p - b) * (p - c))}'
        case _:
            raise ValueError("bruh")
        

print(area({'type': 'triangle', 'sides': [6, 7, 12]}))
print(area({'type': 'circle', 'radius': 67}))
print(area({'type': 'rectangle', 'width': 6, 'height': 7}))