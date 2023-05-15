#Função c/ dois parâmetros

def nome(primeiro_nome, sobrenome):
    print("Meu nome é: ", primeiro_nome, sobrenome)

nome("Marina","Gomes")
nome("Juliana","Mendes")

#Passagem de Paramêtro Por Palavra-Chave

def nomes(pnome, fnome):
    print("Meu nome é: ", pnome, fnome)
    
nomes(pnome="JOSE", fnome="SILVA")



#Mistura de args. posicionais e palavras-chave


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(c=1,b=2,a=3)


#Funções com paramêtros(Mais detalhado)

def name(primeiro_nome, sobrenome="GOMES"):
     print("Olá meu nome é", primeiro_nome, sobrenome)
name("James", "Doe")
 

def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return
    print("Feliz Ano Novo!")
 
#InstruçãoReturn


def boring_function():
    return 123
x = boring_function()
print("A aborrecimento_função retornou seu resultado. Isso é:", x)
 
