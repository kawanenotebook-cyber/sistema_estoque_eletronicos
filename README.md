# Sistema de Controle de Estoque de Eletrônicos (Python)

Sistema completo desenvolvido em Python para o controle interno, cadastro, listagem e baixa de mercadorias em uma loja de eletrônicos. Projeto focado na manipulação de estruturas de dados e tratamento de estoque em tempo real.

# Funcionalidades
- Cadastro Automatizado: Gera códigos identificadores únicos e sequenciais a partir do número 1001 para cada novo item inserido.
- Listagem Detalhada: Exibe todos os produtos salvos na memória com formatação de máscara para moeda brasileira (duas casas decimais).
- Controle de Vendas Dinâmico: Realiza a busca por código, valida se há unidades suficientes e desconta a quantidade vendida de forma cumulativa, emitindo alertas em caso de estoque insuficiente ou ID inválido.
- Menu de Navegação Contínuo: Interface interativa via terminal estruturada através de loops condicionais e encerramento seguro.

# Tecnologias e Conceitos Aplicados
- Modularização e escopo com funções customizadas (def).
- Estruturas de repetição controladas (while True e loops for puros).
- Estruturas de dados avançadas: Listas dinâmicas armazenando Dicionários chave-valor.
- Operadores aritméticos de atribuição acumulativa (-=) para atualização de dados na memória.
- Manipulação e formatação de saídas de tipos Float (:.2f).
