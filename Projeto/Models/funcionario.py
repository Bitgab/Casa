from abc                import ABC, abstractmethod
from Models.fisica      import Fisica
from Models.endereco    import Endereco
from Models.Enums.sexo  import Sexo
from Models.Enums.setor import Setor

class Funcionario(Fisica):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo)
        self.matricula = matricula
        self.setor     = setor
        self.salario   = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"   
            f"\nMatrícula: {self.matricula}"
            f"Setor: {self.setor.value}"
            f"\nSalário: R$ {self.salario} reais"  
            f"\nSalário final: R$ {self.salario_final()} reais"
            )