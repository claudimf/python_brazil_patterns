from classes.cpf import Cpf


cpf = 15616987913
cpf = str(cpf)
tamanho_cpf = len(cpf)
print(tamanho_cpf)

cpf = 15616987913

objeto_cpf = Cpf(cpf)
print(objeto_cpf)

cpf = 156169
objeto_cpf = Cpf(cpf)
print(objeto_cpf)
