class AprioriRules:
    antecedente: str
    consequente: str
    confiança: float
    lift: float
    suporte: float

    def __init__(
        self,
        antecedente: str,
        consequente: str,
        confiança: float,
        lift: float,
        suporte: float,
    ):
        self.antecedente = antecedente
        self.consequente = consequente
        self.confiança = confiança
        self.lift = lift
        self.suporte = suporte

    def __str__(self):
        return (
            f"Antecedente : {self.antecedente} | "
            f"Consequente : {self.consequente} | "
            f"Confiança   : {self.confiança:.2f} | "
            f"Lift        : {self.lift:.2f} | "
            f"Suporte     : {self.suporte:.2%} | "
        )

    __repr__ = __str__
