# while True:
#     linea = input(">")
#     if linea[0] == "#":
#         continue
#     if linea == "fin":
#         break
#     print(linea)
# print("Ciclo terminado")

while True:
    linea = input(">")
    #if len(linea) > 0 and linea[0] == "#":
    if linea.startswith("#"):
        continue
    if linea == "fin":
        break
    print(linea)
print("Ciclo terminado")

# linea = input("")
# l = linea.len()
# print(l)