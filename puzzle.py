from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),                     # A is either a Knight or a Knave
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),                 # A is either a Knight or a Knave
    Or(BKnight, BKnave),                 # B is either a Knight or a Knave
    Biconditional(AKnight, And(AKnave, BKnave))
)
# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),  # A is either a Knight or a Knave
    Or(BKnight, BKnave),  # B is either a Knight or a Knave

    # If A is a Knight, then A's statement "We are the same kind" must be true.
    # This means either both A and B are Knights or both are Knaves.
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # If B is a Knight, then B's statement "We are of different kinds" must be true.
    # This means one of them is a Knight, and the other is a Knave.
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    # If A is a Knave, then A's statement "We are the same kind" must be false.
    # This means one of them is a Knight, and the other is a Knave.
    Biconditional(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    # If B is a Knave, then B's statement "We are of different kinds" must be false.
    # This means either both A and B are Knights or both are Knaves.
    Biconditional(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
   
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight),
    Biconditional(BKnave, CKnight),
    Biconditional(CKnave, AKnave),
    Biconditional(BKnight,AKnave),
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")

if __name__ == "__main__":
    main()
