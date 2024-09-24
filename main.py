'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
Nome = "Paulino"
Nota1 = float(input("Digite sua primeira nota: "))
Nota2 = float(input("Digite sua segunda nota: "))
Nota3 = float(input("Digite sua terceira nota: "))

media= float((Nota1+Nota2+Nota3))

if media >= 30:
    print(Nome,"Aprovado com Distinção!")
    
elif media >= 18:
    print(Nome,"Aprovado!")
    
else:
    print(Nome,"Reprovado.")