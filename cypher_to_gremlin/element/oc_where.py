from typing import List

from cypher_to_gremlin.__spi__.classes import CypherElement, Context
from cypher_to_gremlin.antlr.CypherParser import CypherParser


class OCWhere(CypherElement):

    def __init__(self, elements: List[CypherElement]):
        self.expression = elements[0]

    def execute(self, context: Context) -> str:
        return self.expression.execute(context)

    @staticmethod
    def parse(ctx: CypherParser.OC_WhereContext, supplier):
        return OCWhere(supplier(ctx))

    def __repr__(self):
        return f"WHERE {str(self.expression)}"
