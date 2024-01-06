motorcycles = ['ducati', 'honda', 'suzuki', 'yamaha']
print(motorcycles)

popped_moto = motorcycles.pop()
print(motorcycles)
print(popped_moto)


motorcycles = ['ducati', 'honda', 'suzuki', 'yamaha']
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

motorcycles = ['ducati', 'honda', 'suzuki', 'yamaha']

first_owned = motorcycles.pop(0)
print(f"The first moto I owned was a {first_owned.title()}")

motorcycles = ['ducati', 'honda', 'suzuki', 'yamaha']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['ducati', 'honda', 'suzuki', 'yamaha']
print(motorcycles)

too_fast = 'suzuki'
motorcycles.remove(too_fast)
print(motorcycles)
print(f"\nA {too_fast.title()} is too fast for me!")