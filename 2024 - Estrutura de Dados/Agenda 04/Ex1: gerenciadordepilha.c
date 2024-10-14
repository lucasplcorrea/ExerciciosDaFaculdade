#include <stdio.h>
#include <stdlib.h>

#define MAX 100 // Define a capacidade máxima da pilha

// Estrutura para representar a pilha
typedef struct {
    int itens[MAX];
    int topo; // Índice do topo da pilha
} Pilha;

// Função para inicializar a pilha
void inicializarPilha(Pilha *p) {
    p->topo = -1; // Inicializa o topo da pilha como -1 (indicando que a pilha está vazia)
}

// Função para verificar se a pilha está cheia
int pilhaCheia(Pilha *p) {
    return p->topo == MAX - 1; // Retorna 1 se a pilha estiver cheia
}

// Função para verificar se a pilha está vazia
int pilhaVazia(Pilha *p) {
    return p->topo == -1; // Retorna 1 se a pilha estiver vazia
}

// Função para empilhar um elemento
void empilhar(Pilha *p, int valor) {
    if (pilhaCheia(p)) {
        printf("Pilha cheia! Não é possível empilhar %d.\n", valor);
        return;
    }
    p->itens[++(p->topo)] = valor; // Insere o valor no topo da pilha
    printf("Elemento %d empilhado.\n", valor);
}

// Função para desempilhar um elemento
int desempilhar(Pilha *p) {
    if (pilhaVazia(p)) {
        printf("Pilha vazia! Não é possível desempilhar.\n");
        return -1; // Retorna -1 para indicar que a pilha está vazia
    }
    return p->itens[(p->topo)--]; // Retorna o elemento do topo e decrementa o topo
}

// Função para imprimir os elementos da pilha
void imprimirPilha(Pilha *p) {
    if (pilhaVazia(p)) {
        printf("Pilha vazia!\n");
        return;
    }
    printf("Elementos na pilha: ");
    for (int i = p->topo; i >= 0; i--) {
        printf("%d ", p->itens[i]); // Imprime os elementos do topo para a base
    }
    printf("\n");
}

// Função principal
int main() {
    Pilha p;
    inicializarPilha(&p);

    int opcao, valor;
    
    do {
        printf("\nEscolha uma opção:\n");
        printf("1. Empilhar\n");
        printf("2. Desempilhar\n");
        printf("3. Imprimir a pilha\n");
        printf("4. Sair\n");
        printf("Opção: ");
        scanf("%d", &opcao);
        
        switch (opcao) {
            case 1:
                printf("Digite o valor a empilhar: ");
                scanf("%d", &valor);
                empilhar(&p, valor);
                break;
            case 2:
                valor = desempilhar(&p);
                if (valor != -1) {
                    printf("Elemento desempilhado: %d\n", valor);
                }
                break;
            case 3:
                imprimirPilha(&p);
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
