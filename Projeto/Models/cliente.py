from .endereco import Endereco
from Models.fisica     import Fisica
from Models.Enums.sexo import Sexo

class Cliente(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, protocoloAtendimento: int) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)
        self.protocoloAtendimento = protocoloAtendimento

    def __str__(self) -> str:
        return (  
           f"{super().__str__()}"  
           f"\nNúmero do protocolo de atendimento: {self.protocoloAtendimento}"
           )