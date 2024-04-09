# Format a number to a fixed width in Python

my_int = 12

# ✅ format integer to a fixed width of 3
result = f'{my_int:03d}'
print(result)  # 👉️ '012'

# ✅ format integer to a fixed width of 4
result = f'{my_int:04d}'
print(result)  # 👉️ '0012'

# ✅ format integer to a fixed width of 3 (with leading spaces)
result = f'{my_int:3}'
print(repr(result))  # 👉️ ' 12'

# -----------------------------------

my_float = 1.234567


# ✅ format float to a fixed width of 8 with 3 digits after the decimal

result = f'{my_float:8.3f}'
print(repr(result))  # 👉️ '   1.235'

# -----------------------------------

# ✅ using str.zfill()

result = str(my_int).zfill(3)
print(result)  # 👉️ '012'

result = str(my_int).zfill(4)
print(result)  # 👉️ '0012'