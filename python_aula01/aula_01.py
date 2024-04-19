# python
# Aula 01 - Python

# Comentários

a = 1 # Variável de exemplo para coméntarios 

# docstring

"""
    Este é um comentário 
    que ocupa várias linhas
"""

"""
    que também pode ser
    com aspas simples
"""

print()
print("Se você pretende arricar 'simbolos' diferentes, então faça isso")
print('Ou isso "para alternar" entre aspas simples e duplas')
print()

# print 

print('Teste de saída')
print('Teste de saída \nem várias linhas')
print('Curso','Desenvolvimento de Software')
print('Curso', 'Desenvolvimento de Software', sep='|') #separar as partes utilizando caracteres 
print('Curso', 'Desenvolvimento de Softaware', end='.') #finaliza a string com um determinado caracter
print()
print('Curso \t Desenvolvimento de Software') # separador por tabulador

# Criar um arquivo .txt 
arquivo = open('Aula 01 - saida.txt','a+')

print('Curso', 'Desenvolvimento de Software', file=arquivo)
arquivo.close()

print()

#f5 - Excuta o Script