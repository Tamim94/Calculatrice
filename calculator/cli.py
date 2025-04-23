import argparse
from .calculator import addition, soustraction, multiplication, division

def parse_args():
    """Parse les arguments de la ligne de commande"""
    parser = argparse.ArgumentParser(description='Calculatrice en ligne de commande')
    parser.add_argument('operation', choices=['addition', 'soustraction', 'multiplication', 'division'],
                        help='Opération à effectuer')
    parser.add_argument('a', type=float, help='Premier nombre')
    parser.add_argument('b', type=float, help='Deuxième nombre')

    return parser.parse_args()

def main():
    """Fonction principale qui exécute la calculatrice"""
    args = parse_args()

    try:
        if args.operation == 'addition':
            result = addition(args.a, args.b)
        elif args.operation == 'soustraction':
            result = soustraction(args.a, args.b)
        elif args.operation == 'multiplication':
            result = multiplication(args.a, args.b)
        elif args.operation == 'division':
            result = division(args.a, args.b)

        print(f"Résultat: {result}")

    except ValueError as e:
        print(f"Erreur: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
