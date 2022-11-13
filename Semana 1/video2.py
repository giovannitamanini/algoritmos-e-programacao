arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.read()
print(conteudo)

print()

arquivo = open('arquivo.txt', 'r')
for cont, linha in enumerate(arquivo.readlines()):
  print(str(cont) + '-' + linha)