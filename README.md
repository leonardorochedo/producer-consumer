# Produtor | Consumidor

Resolvendo o problema do produtor e consumidor em Python.

## Objetivo

Construir uma aplicação que simule o processo de produção e consumo de carga em um cenário composto por caminhões, uma doca, uma fábrica e várias lojas. O
objetivo é criar uma solução que garanta a sincronização adequada entre as entidades envolvidas, utilizando semáforos (threads), de modo que o processo ocorra
de forma correta e eficiente.

## Descrição do problema

O cenário envolve dois caminhões, uma doca, uma fábrica e três lojas. Os caminhões são responsáveis por transportar a carga, a doca é o ponto de transferência
da carga entre os caminhões e a fábrica, e as lojas são os locais de venda da carga. O processo acontece da seguinte maneira:

• Os caminhões são criados e iniciam sua execução como threads independentes.
• Os caminhões carregam sua capacidade máxima de carga.
• Os caminhões se dirigem à doca para descarregar a carga.
• A doca, que suporta apenas um caminhão por vez, recebe a carga do caminhão e a transfere para a fábrica.
• A fábrica armazena a carga recebida em seu estoque.
• As lojas, em threads separadas, consomem a carga da fábrica para revenda.
• Após a venda da carga, as lojas ficam sem estoque temporariamente.

O processo se repete, com os caminhões sendo carregados novamente, a carga sendo descarregada na doca, e assim por diante. O objetivo é garantir que a carga
seja transferida corretamente, evitando conflitos e garantindo a sincronização adequada entre as entidades envolvidas.

## Resultados

A implementação do programa permite que o processo de produção e consumo de carga ocorra de forma correta e sincronizada. Os caminhões carregam sua capacidade
máxima de carga, descarregam na doca, a carga é transferida para a fábrica e, em seguida, consumida pelas lojas para venda. O processo se repete de forma
contínua, garantindo a disponibilidade de carga nas lojas e a sincronização correta entre as entidades envolvidas.

## Conclusão

O problema do produtor e consumidor é um desafio comum na área de programação concorrente. Neste projeto, foi apresentada uma solução em Python para simular o
processo de produção e consumo de carga em um cenário composto por caminhões, doca, fábrica e lojas. A implementação utiliza threads e semáforos para garantir a
sincronização adequada e evitar conflitos entre as entidades envolvidas.

Espero que este projeto tenha ajudado a compreender melhor o problema do produtor e consumidor e a aplicação de conceitos de concorrência em Python.
