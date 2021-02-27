"The Interpreter Pattern Use Case Example"

from sentence_parser import Parser

# The sentence complies with a simple grammar of
# Number -> Operator -> Number -> etc,
SENTENCE = "5 + IV - 3 + VII - 2"
# SENTENCE = "V + IV - III + 7 - II"
# SENTENCE= "CIX + V"
# SENTENCE = "CIX + V - 3 + VII - 2"
# SENTENCE = "MMMCMXCIX - CXIX + MCXXII - MMMCDXII - XVIII - CCXXXV"
print(SENTENCE)

AST_ROOT = Parser.parse(SENTENCE)

# Interpret recursively through the full AST starting from the root.
print(AST_ROOT.interpret())

# Print out a representation of the AST_ROOT
print(AST_ROOT)
