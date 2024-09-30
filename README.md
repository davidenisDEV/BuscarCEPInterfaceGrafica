## Projeto 2: Buscador de CEP - Interface Gráfica com PySimpleGUI

### Descrição

Este projeto é um buscador de CEP simples desenvolvido com **Python**, utilizando a biblioteca **PySimpleGUI** para a interface gráfica e **PyCep** para realizar a consulta de informações sobre o CEP. O aplicativo permite que o usuário insira um CEP e obtenha dados como o nome da rua, bairro, cidade e estado.

### Funcionalidades

- Busca informações de endereço a partir de um CEP.
- Exibe o resultado diretamente na interface gráfica.
- Opção de salvar o CEP inserido (marcador visual, sem funcionalidade de persistência).

### Exemplo de Saída

```
CEP: 01001-000
UF: SP
Cidade: São Paulo
Bairro: Sé
O nome da rua: Praça da Sé
```

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado e as bibliotecas necessárias.

1. Instale as dependências:

   ```bash
   pip install pysimplegui pycep
   ```

### Como Usar

1. Clone o repositório e navegue até o diretório:

   ```bash
   git clone https://github.com/seu-usuario/Buscador-CEP.git
   cd Buscador-CEP
   ```

2. Execute o script `buscador_cep.py` com o Python:

   ```bash
   python buscador_cep.py
   ```

3. A interface será aberta, permitindo que você insira o CEP e faça a consulta.

### Personalizações

- **Tema**: Para alterar o tema da interface, modifique `sg.theme('SystemDefault')` para outros temas como `'DarkBlue'`, `'LightGrey'`, etc.
- **Funcionalidade de Salvar CEP**: Atualmente, a checkbox "Salvar CEP?" não possui funcionalidade. Para implementá-la, você pode desenvolver um método para salvar o CEP em um arquivo ou banco de dados.

