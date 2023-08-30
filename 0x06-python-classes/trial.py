print("Hi R")
def raise_error():
    return
try:
    t = raise_error()
except Exception as e:
    print(e)
print(t)
