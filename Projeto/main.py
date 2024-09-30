import os 
from Projeto.Models.advogado                    import Advogado
from Projeto.Models.cliente                     import Cliente
from Projeto.Models.fisica                      import Fisica
from Projeto.Models.funcionario                 import Funcionario
from Projeto.Models.juridica                    import Juridico
from Projeto.Models.medico                      import Medico
from Projeto.Models.engenheiro                  import Engenheiro
from Projeto.Models.pessoa                      import Pessoa
from Projeto.Models.endereco                    import Endereco
from Projeto.Models.Enums.estadocivil           import EstadoCivil
from Projeto.Models.Enums.setor                 import Setor
from Projeto.Models.Enums.sexo                  import Sexo
from Projeto.Models.Enums.unidadeFederativa     import UnidadeFederativa

os.system("cls || clear")

advogado    = Advogado("Samir santos", "(71) 91234-5678","Samiroab2gmail.com.oab",Endereco("Rua A",12,"Perto da Casa Branca","00.000-000","Nova York",UnidadeFederativa.BAHIA) ,"123.345.678-90","12.345.678.90","12/09/2024",Sexo.MASCULINO, "120924", Setor.JURIDICO,10000.00, "120345")
medico      = Medico("Rafael Dias", "(71) 91234-5678","Rafael@gmail.com",Endereco("Rua B", 6, "Perto do senai", "12.345-0000","Salvador", UnidadeFederativa.BAHIA),"123.456.789-00","98.765.432-12","12/09/2024",Sexo.MASCULINO,"110924",Setor.ENGENHARIA,10000.00,"12345")
engenheiro  = Engenheiro("Gabriel","(71) 95678-4321","gabriel@gmail.com",Endereco("Rua C",7,"Perto do merdado","00.235-000","Vera Cruz", UnidadeFederativa.BAHIA),"123.456.789-00","12.345.678-90","20/09/2024",Sexo.MASCULINO, "120924", Setor.OPERACOES, 1200,"1234546")
print(advogado)
print(medico)
print(engenheiro)