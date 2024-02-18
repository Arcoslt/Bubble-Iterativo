from random import randint

def main():
    tamanho = input('Tamanho do Vetor: ')
    tamanho = int(tamanho)
    vet = []

    for i in range(tamanho):
        vet.append(randint(1, tamanho))

    for i in range(tamanho-1):
        for j in range(tamanho-1-i):
            #Troca pos do vet com a do proximo, caso o proximo seja menor que o atual
            if vet[j]>vet[j+1]:
                aux=vet[j+1]
                vet[j+1]=vet[j]
                vet[j]=aux
    
    for i in range(tamanho):
        print(vet[i])

if __name__ == "__main__":
    main()
