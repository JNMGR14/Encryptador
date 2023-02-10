def codex(msj):
    print("Mensaje incriptado: ", end="")
    key_word = 'MURCIELAGO'
    key = {value: key for (key, value) in enumerate(key_word)}
    for x in msj:
        print(key[x], end="") if x in key else print(x, end="")
    print("")


if __name__ == '__main__':
    while True:
        codex(input("Ingrese la palabra a incriptar:").upper())
