"""
В магазинах имеются следующие товары. Магнит - молоко, соль, сахар.
Пятерочка - мясо, молоко, сыр. Перекресток - молоко, творог, сыр, сахар. Определить:
1. полный список всех товаров
2. в каких магазинах можно приобрести одновременно молоко и сыр.
3. в каких магазинах можно приобрести сахар.
"""

magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}

all_products = set()
for product in magnit|pyaterochka|perekrestok:
  if product not in all_products:
    all_products.add(product)

print("Полный список всех товаров:")
print(sorted(all_products))
print()

print("Магазины, где можно купить одновременно молоко и сыр:")
if "молоко" in magnit and "сыр" in magnit:
  print("Магнит")
if "молоко" in pyaterochka and "сыр" in pyaterochka:
  print("Пятерочка")
if "молоко" in perekrestok and "сыр" in perekrestok:
  print("Перекресток")
print()

print("Магазины, где можно купить сахар:")
if "сахар" in magnit:
  print("Магнит")
if "сахар" in pyaterochka:
  print("Пятерочка")
if "сахар" in perekrestok:
  print("Перекресток")