# =========================================
# USING CUSTOM MODULE
# =========================================

import custom_module

print(custom_module.add(5, 3))
print(custom_module.greet("Aryan"))

# from custom_module import add

# print(add(10, 20))

from packages.math_utils import multiply
from packages.string_utils import to_upper

print(multiply(4, 5))
print(to_upper("python"))

import math
import random

print(math.sqrt(16))
print(random.randint(1, 10))