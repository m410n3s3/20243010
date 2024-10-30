nomes = ("gu", "vi", "ma", "ka")

try:
    for i in range(4):
        print(nomes[i])

except IndexError as erro:
    print("houve um erro")
    print(erro)

else:
    print("programa não passou com erro")
print("L7")

