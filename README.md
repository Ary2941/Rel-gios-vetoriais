# Implementação de relógios vetoriais
    Entrega: 15/03/2024
    Equipe: dupla

## Objetivos
    - Implementar a lógica de relógios vetoriais em uma linguagem de programação adequada para sistemas distribuídos
    
    - Realizar testes extensivos para validar a corretude e a eficiência da implementação através de uma simulação

## Implementação
    - Escolha de uma linguagem de programação adequada para sistemas distribuídos, como Java, Python ou C++
    
    - Utilize sockets ou gRPC
    
    - Desenvolvimento da lógica de relógios vetoriais, incluindo estruturas de dados e algoritmos necessários para seu funcionamento

## Teste e validação
    - Considere um cenário onde mensagens são trocadas entre vários processos aleatoriamente entre os processos de tempos em tempos (tempo aleatório para envio de mensagens). Por exemplo, considere um sistema distribuído composto por 4 processos, eles trocarão mensagens entre si repassando seus vetores
    
    - Para cada processo, defina uma porta especifica, (por exemplo: p1, porta 5001, p2, porta 5002 etc) e todos os processos sabem as portas de todos para enviar mensagens aleatórias
    
    - Observe que, no momento de enviar uma mensagem, o processo emissor selecionará uma porta de processo aleatoriamente e enviará uma mensagem e o vetor que está enviando. O processo emissor deverá imprimir na tela o vetor que está enviando.
    - Ao receber a mensagem, o processo receptor deverá imprimir na tela o vetor recebido, o próprio vetor e o vetor resultante
    - O intervalo de envio de mensagens deve variar entre 1s e 4s

## Envio
    - Código fonte + nomes dos integrantes da equipe; ou
    
    - Arquivo txt com link do github (no projeto deve conter o nme da dupla)