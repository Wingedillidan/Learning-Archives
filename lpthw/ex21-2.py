from ex21 import *

result = add(24, subtract(divide(34., 100.), 1023))
print result

# 8210 - 30 / 3 * 294 + 69 / 2091 * 29
result = add(subtract(8210, multiply(294, divide(30., 3))), multiply(29, divide(69., 2091)))
print result