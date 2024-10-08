def temp_media(cidades_temp):
    media_cidade = []
    for cidade, temperaturas in cidades_temp:
        media = sum(temperaturas) / len(temperaturas)
        media_cidade.append((cidade, media))
    return media_cidade

cidades_temp = [
    ("São Paulo", [20, 21, 23, 28, 25, 19, 27]),
    ("Rio de Janeiro ", [24, 27, 28, 30, 33, 31, 29]),
    ("Belo Horizonte", [17, 19, 21, 20, 23, 26, 30])
]

result = temp_media(cidades_temp)
print(result)