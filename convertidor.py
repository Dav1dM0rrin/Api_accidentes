with open("datos.json", "r", encoding="utf-16") as f:
    data = f.read()

with open("datos_utf8.json", "w", encoding="utf-8") as f:
    f.write(data)

print("Archivo convertido a UTF-8 correctamente.")
