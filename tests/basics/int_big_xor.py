print(0 ^ (1 << 80))
print((1 << 80) ^ (1 << 80))
print((1 << 80) ^ 0)

a = 0xfffffffffffffffffffffffffffff
print(a ^ (1 << 100))
print(a ^ (1 << 200))
print(a ^ a == 0)
print(bool(a ^ a))
