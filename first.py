def gen_with_error():
    yield 1
    raise ValueError("Error inside generator")

g = gen_with_error()
print(next(g))
try:
    g.throw(ValueError, "Error thrown")
except ValueError as e:
    print(e)