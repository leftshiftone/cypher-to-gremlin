from cypher_to_gremlin.__spi__.classes import CypherElement, Context
from cypher_to_gremlin.antlr.CypherParser import CypherParser


class OCPropertyLookup(CypherElement):

    def __init__(self, name: str):
        self.name = name

    def execute(self, context: Context) -> str:
        return self.name

    @staticmethod
    def parse(ctx: CypherParser.OC_PropertyLookupContext, _supplier):
        return OCPropertyLookup(ctx.getText()[1:])

    def __repr__(self):
        return f".{self.name}"
