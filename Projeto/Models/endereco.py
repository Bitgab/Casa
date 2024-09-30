from Models.Enums.unidadeFederativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: int, complamento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.lougradouro = logradouro
        self.numero      = numero
        self.complemento = complamento
        self.cep         = cep
        self.cidade      = cidade
        self.uf          = uf

    def __str__(self) -> str:
        return (
            f"\nLogradouro: {self.lougradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
            f"\nUf: {self.uf}"
        )    