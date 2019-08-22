from bissexto import ano_bissexto

def test_ano_bissexto_divisivel_por_400():
    assert ano_bissexto(1600)

def test_ano_bissexto_divisivel_por_4():
    assert ano_bissexto(1732)
    assert ano_bissexto(1888)
    assert ano_bissexto(1944)
    assert ano_bissexto(2008)

def test_nao_ano_bissexto_divisivel_por_100():
    assert not ano_bissexto(1000)

def test_nao_ano_bissexto_nao_divisivel_por_4():
    assert not ano_bissexto(1742)
    assert not ano_bissexto(1889)
    assert not ano_bissexto(1951)
    assert not ano_bissexto(2011)