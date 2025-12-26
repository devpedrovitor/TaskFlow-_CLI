# 📋 TaskFlow CLI  
**VERSÃO 1.0**

Gerenciador de tarefas simples desenvolvido em **Python**, executado via terminal (**CLI – Command Line Interface**), permitindo o controle básico de tarefas pessoais.

---

## 📌 Descrição

O **TaskFlow CLI** é um projeto de estudo focado no aprendizado de lógica de programação e fundamentos do Python, utilizando listas, dicionários, funções e interação com o usuário no terminal.  
As tarefas são armazenadas apenas em memória durante a execução do programa.

CLI (Command Line Interface) significa que a interação com o usuário é feita **digitando comandos ou opções no terminal**, sem interface gráfica.

---

## ⚙️ Funcionalidades

- Adicionar tarefas  
- Visualizar todas as tarefas  
- Editar tarefas  
- Visualizar tarefas concluídas  
- Excluir tarefas concluídas  
- Menu interativo no terminal  

---

## 🗂️ Estrutura das Tarefas

```python
{
    "id": int,
    "name_task": str,
    "tipo_task": str,
    "data_inicio": str,
    "data_vencimento": str,
    "Complete": bool
}
```

## ▶️ Como Executar

### Pré-requisitos
- Python 3.x instalado

### Execução
```bash
python main.py
```

## 📜 Menu do Sistema

---- Gerenciador de tarefas ----
1. Adicionar tarefas
2. Ver tarefas
3. Editar tarefas
4. Ver tarefas completas
5. Deletar tarefas completas
6. Sair

## 🛠️ Tecnologias Utilizadas

* **Python 3**: Linguagem principal do projeto.
* **Terminal (CLI)**: Interface de linha de comando para interação com o usuário.

---

## 🚀 Melhorias Futuras

Para evoluir o projeto, as seguintes funcionalidades e refatorações estão no radar:

- [ ] **Persistência de dados**: Implementação de salvamento em arquivos JSON.
- [ ] **Validação de dados**: Tratamento de exceções e validação de formatos de data.
- [ ] **Interface Gráfica (GUI)**: Migração do CLI para uma interface visual (ex: Tkinter ou PySide).
- [ ] **Programação Orientada a Objetos (POO)**: Refatoração do código para utilizar classes e métodos, aumentando a escalabilidade.

---

## 📚 Objetivo

O foco principal deste repositório é o **aprendizado prático**. Ele serve como base para consolidar o entendimento sobre lógica de programação, manipulação de variáveis, estruturas de repetição e funções em Python.

---

## 💡 Contribuições

Feedbacks e sugestões são muito bem-vindos! Se você deseja contribuir para a evolução deste projeto:

1.  Abra uma **Issue** para discutir novas ideias.
2.  Envie um **Pull Request** com melhorias de código ou correções.
3.  Compartilhe ideias para novas funcionalidades que desafiem a lógica atual.

---

