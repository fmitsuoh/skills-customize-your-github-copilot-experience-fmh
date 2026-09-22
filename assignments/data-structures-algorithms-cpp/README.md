# 📘 Tarefa: Estruturas de Dados e Algoritmos em C++

## 🎯 Objective

Aprenda a implementar algoritmos clássicos de busca e ordenação em C++ utilizando `std::vector`, entendendo como a organização dos dados afeta a eficiência dos algoritmos.

## 📝 Tasks

### 🛠️ Busca Linear

#### Descrição
Implemente a função `linearSearch` que percorre um `vector<int>` procurando um valor alvo.

#### Requisitos
O programa completo deve:

- Definir `int linearSearch(const std::vector<int>& values, int target)`
- Retornar o índice da primeira ocorrência de `target`, ou `-1` caso não seja encontrado
- Testar a função com um vetor de exemplo e imprimir o resultado

### 🛠️ Busca Binária

#### Descrição
Implemente a função `binarySearch` para um `vector<int>` já ordenado, usando a abordagem iterativa.

#### Requisitos
O programa completo deve:

- Definir `int binarySearch(const std::vector<int>& values, int target)`
- Assumir que `values` está ordenado em ordem crescente
- Retornar o índice de `target`, ou `-1` caso não seja encontrado
- Comparar o número de passos necessários com o da busca linear para o mesmo valor

### 🛠️ Ordenação e Integração

#### Descrição
Implemente a função `insertionSort` para ordenar um `vector<int>` e utilize-a antes de aplicar a busca binária em um conjunto de dados desordenado.

#### Requisitos
O programa completo deve:

- Definir `void insertionSort(std::vector<int>& values)` que ordene o vetor in-place em ordem crescente
- Receber um vetor desordenado, ordená-lo com `insertionSort` e em seguida buscar um valor com `binarySearch`
- Imprimir o vetor antes e depois da ordenação, e o índice encontrado na busca
