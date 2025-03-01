# Problemas de Importação em Python e Manipulação do PYTHONPATH

## Estrutura de Pacotes e Módulos em Python

O Python organiza o código em **módulos** e **pacotes**. Um módulo é um arquivo `.py`, enquanto um pacote é uma pasta contendo um arquivo `__init__.py` (opcional no Python 3.3+).

Exemplo de estrutura de diretórios:

```
projeto/
│-- main.py
│-- modulo1.py
│-- pasta/
│   │-- __init__.py
│   │-- modulo2.py
```

## Importação Relativa e Absoluta

### Importação Absoluta
A importação absoluta exige o caminho completo do módulo a partir do diretório raiz do projeto:

```python
# Dentro de main.py
import pasta.modulo2
```

### Importação Relativa
Dentro de `modulo2.py`, podemos usar importação relativa:

```python
# Dentro de modulo2.py
from .. import modulo1  # Importa modulo1.py que está no diretório superior
```

Isso só funciona se `modulo2.py` for parte de um pacote, ou seja, se for executado como parte de um contexto de pacote, não diretamente via `python modulo2.py`.

## Problemas com Importação

### Erro de Importação por Execução Direta
Se você executar um arquivo diretamente (por exemplo, `python pasta/modulo2.py`), o Python pode falhar ao resolver importações relativas. O erro comum é:

```
ImportError: attempted relative import with no known parent package
```

### Como Resolver
#### 1. Executar o script a partir do diretório raiz do projeto
```sh
python -m pasta.modulo2
```
Isso permite que o Python reconheça o pacote corretamente.

#### 2. Modificar `sys.path` para incluir o diretório raiz do projeto
Dentro de `modulo2.py`:

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import modulo1  # Agora funciona
```

#### 3. Configurar o PYTHONPATH
Podemos adicionar o diretório raiz do projeto ao `PYTHONPATH`:

```sh
export PYTHONPATH=$(pwd)
python pasta/modulo2.py
```

## Conclusão
O Python não enxerga automaticamente módulos em subdiretórios ou diretórios superiores sem a configuração adequada. Manipular o `PYTHONPATH` ou utilizar execução como módulo são soluções comuns para resolver esses problemas.

