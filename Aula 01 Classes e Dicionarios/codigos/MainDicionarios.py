# Dicionários

# Declarando um dicionário
Endereco = {}

# Adicionando elementos no dicionário
Endereco["rua"] = "rua deputado lusca"

print(Endereco)

# Deletando um elemento do dicionário
Endereco.pop("rua")

print(Endereco)

# Iterando sobre as chaves e sobre os valores do dicionário
nomes = {
    "joao" : "gabriel", 
    "lucas" : "farias"
}

for chave in nomes:
    print(chave + "\n")
for valores in nomes.values():
    print(valores + "\n")


# Acessando um item individual do dicionário

nome_bacana = nomes["joao"]

print(nome_bacana)

print(nomes["lucas"])


# colocando mais de um valor na mesma chave
# usando lista

cores = {
    "primarias":["vermelho","azul","amarelo"],
    "secundarias":["laranja","roxo","verde"]
}

print(cores["primarias"])
print(cores["secundarias"])

# usando outro dicionário

Locadora = {
    "filmeA":{
        "nome": "drive",
        "ano" : 2014,
        "nota" : 8.8
    },
    "filmeB":{
        "nome": "pulp fiction",
        "ano": 1994,
        "nota": 9.5
    }
}

print(Locadora["filmeA"])
print(Locadora["filmeA"]["nome"])



