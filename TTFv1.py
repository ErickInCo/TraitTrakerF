from typing import List

class Champion:
    def __init__(self, name: str, cost: int, traits: List[str], ability: str):
        """
        Inicializa un campeón de TFT.

        :param name: Nombre del campeón
        :param cost: Costo del campeón (generalmente de 1 a 5)
        :param traits: Lista de rasgos a los que pertenece el campeón
        :param ability: Descripción de su habilidad principal
        """
        self.name = name
        self.cost = cost
        self.traits = traits
        self.ability = ability

    def __repr__(self):
        return f"Champion(name='{self.name}', cost={self.cost}, traits={self.traits})"

    def has_trait(self, trait: str) -> bool:
        """Verifica si el campeón tiene un rasgo específico."""
        return trait in self.traits
    
    