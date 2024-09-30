import pytest
from Models.advogado import Advogado
from Models.endereco import Endereco
from Models.Enums.unidadeFederativa import UnidadeFederativa
from Models.Enums.sexo import Sexo
from Models.Enums.setor import Setor

def test_advogado():
    advogado = Advogado("Rafael", "(71) 91234-5678", "fuboca@gmail.com",Endereco("Rua A", 12, "Perto do senai", "123.45-678", "Salvador",UnidadeFederativa.BAHIA)
    ,"123.456.789-00", "12.345.678-66","02/08/2001",Sexo.MASCULINO,"12345",Setor.JURIDICO, 10000)

    assert advogado.nome == "Rafael"
    assert advogado.telefone == "(71) 91234-5678"
    
   