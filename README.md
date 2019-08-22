## ANO BISSEXTO
Esta aplicação tem como objetivo retornar se um determinado ano é ou não bissexto.

### Para executar a aplicação em uma máquina virtual:

* Preparando o ambiente (linux):
`virtualenv -p python3 env`
`source env/bin/activate`
`pip install -r requirements.txt`

* Executando Aplicação:
`python bissexto.py <ano>`

* Executando testes:
`pytest test.py`