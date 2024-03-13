# Implementação de Relógios Vetoriais

Este projeto consiste na implementação da lógica de relógios vetoriais em Python para sistemas distribuídos, conforme especificado na tarefa. A implementação inclui testes extensivos para validar a corretude e eficiência da solução através de uma simulação.

## Implementação
envio de mensagens via socket TCP

## Equipe

Este projeto foi desenvolvido por:

- [Aamaury Junior](https://github.com/Ary2941)

## Objetivos

- Implementar a lógica de relógios vetoriais em Python.
- Realizar testes extensivos para validar a corretude e eficiência da implementação.
- Utilizar sockets para comunicação entre processos.
- Simular troca de mensagens entre vários processos em intervalos aleatórios.

## Implementação

- Linguagem de Programação: Python 3.12
- Dependências: Nenhuma

## Execução

Para executar o programa, utilize o seguinte comando:

```bash
python vector.py `<porta>`
```

Onde `<porta>` é a porta na qual o processo será executado.

## Comandos
```bash
 send <endereço_do_processo>
```
Envia o vetor do processo para o processo com o endereço especificado, sendo `<endereço_do_processo>` é a porta na qual o vetor será enviado


```bash
p
```
Simula um evento dentro do processo.
```bash
neo <endereço_do_processo>(,<endereço_do_processo>)*
```
O processo envia randomicamente entre uma lista de processos, sendo `<endereço_do_processo>` é a porta na qual o vetor será enviado

## Teste e Validação
O teste e validação do sistema são realizados por meio de uma simulação onde mensagens são trocadas entre vários processos aleatoriamente em intervalos de tempo aleatórios ou pelo envio de processo para processo diretamente via comandos no terminal
