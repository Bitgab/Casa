from Models.endereco    import Endereco
from Models.funcionario import Funcionario
from Models.Enums.sexo  import Sexo
from Models.Enums.setor import Setor

class Medico(Funcionario):
    BONIFICACAO = 1.5
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)
        self.crm  = crm

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado

    def __str__(self) -> str:
        return ( 
            f"{super().__str__()}"
            f"\nCRM: {self.crm}" 
            )