import math
from pyGL20 import GPIO

IO = GPIO(0)

def square_root(x):
  y = math.sqrt(x)
  IO.digitalWriteToggleAll()
  return y + 2

def GL20_digitalWriteToggleAll():
  IO.digitalWriteToggleAll()
