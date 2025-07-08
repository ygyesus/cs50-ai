from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

universal = And(
    Not(And(AKnight, AKnave)), Or(AKnight, AKnave),
    Not(And(BKnight, BKnave)), Or(BKnight, BKnave),
    Not(And(CKnight, CKnave)), Or(CKnight, CKnave)
)
# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    # TODO
    universal,
    Biconditional(
        AKnight, 
        And(AKnight, AKnave)
    )
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASays = And(AKnave, BKnave)
knowledge1 = And(
    # TODO
    universal,
    Biconditional(
        AKnight, ASays
    ),
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."

ASays = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)

BSays = Or(
    And(AKnave, BKnight),
    And(AKnight, BKnave)
)

knowledge2 = And(
    # TODO
    universal,
    Biconditional(AKnight, ASays),
    Biconditional(BKnight, BSays)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.  
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

udk_which = Symbol("You don't know which")
udk_which = Or(AKnight, AKnave)

ASays = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    udk_which
)

BSays = And(
    Or(
        And(AKnight, AKnave),
        And(AKnave, AKnave)
    ),
    CKnave
)

CSays = AKnight


knowledge3 = And(
    # TODO
    universal,
    Biconditional(
        AKnight, ASays 
    ),
    Biconditional(BKnight, BSays),
    Biconditional(CKnight, CSays)



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
