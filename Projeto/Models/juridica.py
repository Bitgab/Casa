from Models.pessoa   import Pessoa
from Models.endereco import Endereco

class Juridico(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cnpj:str, inscricaoEstadual: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj              = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return ( 
            f"{super().__str__()} "
            f"\nCNPJ: {self.cnpj}"
            f"Inscrição Estadual: {self.inscricaoEstadual}"    
            )
       