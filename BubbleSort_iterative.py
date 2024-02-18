from random import sample

def main():
    #Criação do vetor com tamanho desejado e com inteiros aleatórios
    tamanho = input('Tamanho do Vetor: ')
    tamanho = int(tamanho)
    vet = []
    #Sample não repete números, fica mais fácil a visualização dop Bubble
    vet = sample(range(1, tamanho + 1), tamanho)
    print("Vetor desordenado:",vet)

    #Bubble sort
    for i in range(tamanho-1):
        for j in range(tamanho-1-i):
            #Troca posição do vet com a do próximo, caso o proximo seja menor que o atual
            if vet[j]>vet[j+1]:
                aux=vet[j+1]
                vet[j+1]=vet[j]
                vet[j]=aux

    print("Vetor ordenado:",vet)

if __name__ == "__main__":
    main()
