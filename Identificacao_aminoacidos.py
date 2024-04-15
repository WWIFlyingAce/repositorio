import re

sequencia = input("Digite a sequência de RNA:")
sequencia = sequencia.upper()
numero_bases = len(sequencia)
codons = re.split("(\S{3})", sequencia)
codons = list(filter(None, codons))
  
aminoacidos = []

for item in codons:
    if item == "UUU" or item == "UUC":
        aminoacidos.append("Fenilalanina")
    elif item == "UUA" or item == "UUG" or item == "CUU" or item == "CUC" or item == "CUA" or item == "CUG":
        aminoacidos.append("Leucina")
    elif item == "UCU" or item == "UCC" or item == "UCA" or item == "UCG" or item == "AGU" or item == "AGC":
        aminoacidos.append("Serina")
    elif item == "UAU" or item == "UAC":
        aminoacidos.append("Tirosina")
    elif item == "UAA" or item == "UAG" or item == "UGA":
        aminoacidos.append("Códon Final")
    elif item == "UGU" or item == "UGC":
        aminoacidos.append("Cisteína")
    elif item == "UGG":
        aminoacidos.append("Triptofano")
    elif item == "CCU" or item == "CCC" or item == "CCA" or item == "CCG":
        aminoacidos.append("Prolina")
    elif item == "CAU" or item == "CAC":
        aminoacidos.append("Histidina")
    elif item == "CAA" or item == "CAG":
        aminoacidos.append("Glutamina")
    elif item == "CGU" or item == "CGC" or item == "CGA" or item == "CGG" or item == "AGA" or item == "AGG":
        aminoacidos.append("Arginina")
    elif item == "AUU" or item == "AUC" or item == "AUA":
        aminoacidos.append("Isoleucina")
    elif item ==  "AUG":
        aminoacidos.append("(Códon Inicial) Metionina")
    elif item == "ACU" or item == "ACC" or item == "ACA" or item == "ACG":
        aminoacidos.append("Treonina")
    elif item == "AAU" or item == "AAC":
        aminoacidos.append("Asparagina")
    elif item == "AAA" or item == "AAG":
        aminoacidos.append("Lisina")
    elif item == "GUU" or item == "GUC" or item == "GUA" or item == "GUG":
        aminoacidos.append("Valina")
    elif item == "GCU" or item == "GCC" or item == "GCA" or item == "GCG":
        aminoacidos.append("Alanina")
    elif item == "GAU" or item == "GAC":
        aminoacidos.append("Ácido Aspártico")
    elif item == "GAA" or item == "GAG":
        aminoacidos.append("Ácido Glutâmico")
    elif item == "GGU" or item == "GGC" or item == "GGA" or item == "GGG":
        aminoacidos.append("Glicina")
    else:
        aminoacidos.append("Códon não identificado!")

if numero_bases % 3 != 0:
    print("A sequência de RNA está incompleta!")
elif codons[0] != "AUG":
    print("O códon inicial do RNA está incorreto!")
else: 
    print(f"A sequência de códons é: {codons}")    
    print(f"A sequência de aminoacidos é: {aminoacidos}")          
