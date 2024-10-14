#include <stdio.h>
#include <stdlib.h>

#define MAX 100 // Define a capacidade máxima da fila

// Estrutura para representar a fila
typedef struct {
    int itens[MAX];
    int frente; // Índice do primeiro elemento
    int tras;   // Índice do último elemento
} Fila;

// Função para inicializar a fila
void inicializarFila(Fila *f) {
    f->frente = 0; // Inicializa a frente da fila
    f->tras = -1;  // Inicializa o tras da fila
}

// Função para verificar se a fila está cheia
int filaCheia(Fila *f) {
    return (f->tras + 1) % MAX == f->frente; // Retorna 1 se a fila estiver cheia
}

// Função para verificar se a fila está vazia
int filaVazia(Fila *f) {
    return f->frente == (f->tras + 1) % MAX; // Retorna 1 se a fila estiver vazia
}

// Função para enfileirar um elemento
void enfileirar(Fila *f, int valor) {
    if (filaCheia(f)) {
        printf("Fila cheia! Não é possível enfileirar %d.\n", valor);
        return;
    }
    f->tras = (f->tras + 1) % MAX; // Move o índice do último elemento
    f->itens[f->tras] = valor;     // Insere o valor na fila
    printf("Elemento %d enfileirado.\n", valor);
}

// Função para desenfileirar um elemento
int desenfileirar(Fila *f) {
    if (filaVazia(f)) {
        printf("Fila vazia! Não é possível desenfileirar.\n");
        return -1; // Retorna -1 para indicar que a fila está vazia
    }
    int valor = f->itens[f->frente]; // Armazena o valor a ser retornado
    f->frente = (f->frente + 1) % MAX; // Move o índice da frente
    return valor; // Retorna o valor desenfileirado
}

// Função para imprimir os elementos da fila
void imprimirFila(Fila *f) {
    if (filaVazia(f)) {
        printf("Fila vazia!\n");
        return;
    }
    printf("Elementos na fila: ");
    for (int i = f->frente; i != (f->tras + 1) % MAX; i = (i + 1) % MAX) {
        printf("%d ", f->itens[i]); // Imprime os elementos da fila
    }
    printf("\n");
}

// Função principal
int main() {
    Fila f;
    inicializarFila(&f);

    int opcao, valor;

    do {
        printf("\nEscolha uma opção:\n");
        printf("1. Enfileirar\n");
        printf("2. Desenfileirar\n");
        printf("3. Imprimir a fila\n");
        printf("4. Sair\n");
        printf("Opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite o valor a enfileirar: ");
                scanf("%d", &valor);
                enfileirar(&f, valor);
                break;
            case 2:
                valor = desenfileirar(&f);
                if (valor != -1) {
                    printf("Elemento desenfileirado: %d\n", valor);
                }
                break;
            case 3:
                imprimirFila(&f);
                break;
            case 4:
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    } while (opcao != 4);

    return 0;
}
