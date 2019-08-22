# ANO BISSEXTO
Esta aplicação tem como objetivo retornar se um determinado ano é ou não bissexto.

## Para executar a aplicação em uma máquina virtual:

### Preparando o ambiente (linux):
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

### Executando Aplicação:
`python bissexto.py <ano>`

* Você poder adicionar quantos anos quiser na linha acima. Exemplo:
`python bissexto.py 2000 2019 1000`

### Executando testes:
`pytest test.py`