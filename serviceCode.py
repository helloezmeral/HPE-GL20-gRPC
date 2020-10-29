import math
import pyGL20

IO = pyGL20.GPIO(0)

# def GL20_digitalWriteToggleAll():
#   IO.digitalWriteToggleAll()

def digitalWriteToggle(pin):
  if pin in range(6,8):
    IO.digitalWriteToggle(IO.PIN(pin))
    return True
  else:
    return False
  
def digitalWriteToggleAll():
  IO.digitalWriteToggleAll()
  return True

def digitalReadAll() -> int:
  return IO.digitalReadAll()

def digitalRead(pin) -> bool:
  return IO.digitalRead(IO.PIN(pin))

def digitalWriteAll(value) -> int:
  return IO.digitalWriteAll(value)

def digitalWrite(pin, level) -> bool:
  return IO.digitalWrite(IO.PIN(pin), level)