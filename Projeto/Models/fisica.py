from abc               import ABC, abstractmethod
from .endereco         import Endereco
from Models.pessoa     import Pessoa
from Models.Enums.sexo import Sexo

class Fisica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf            = cpf
        self.rg             = rg
        self.dataNascimento = dataNascimento
        self.sexo           = sexo

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nData de nascimento: {self.dataNascimento}"
            f"\nSexo: {self.sexo.value}"
            )  