from Models.funcionario import Funcionario
from Models.endereco    import Endereco
from Models.Enums.sexo  import Sexo
from Models.Enums.setor import Setor

class Engenheiro(Funcionario):
    BONIFICACAO = 1.3
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, dataNascimento: str, sexo: Sexo, matricula: str, setor: Setor, salario: float, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, dataNascimento, sexo, matricula, setor, salario)
        self.crea = crea

    def salario_final(self) -> float:
       resultado = self.salario * self.BONIFICACAO
       return resultado  

    def __str__(self) -> str:
        return (  
                f"{super().__str__()}"
                f"\nCREA: {self.crea}" 
               )