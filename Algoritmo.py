def balance(expr):
    opens = {'(': ')', '[': ']', '{': '}'}
    stack, steps = [], []
    for c in expr:
        if c in opens:
            stack.append(c)
            steps.append(f"PUSH {c}, stack={stack}")
        elif c in opens.values():
            if not stack:
                steps.append(f"ERROR: unmatched {c}")
                return False, steps
            top = stack.pop()
            if opens[top] != c:
                steps.append(f"ERROR: {top} != {c}")
                return False, steps
            steps.append(f"POP {top} for {c}, stack={stack}")
    if stack:
        steps.append(f"ERROR: leftovers {stack}")
        return False, steps
    steps.append("ALL MATCHED")
    return True, steps

def main():
    with open('expresiones.txt') as f:
        for linea in f:
            expr = linea.strip()
            print(f"Expr: {expr}")
            ok, log = balance(expr)
            for paso in log:
                print("  ", paso)
            print("RESULTADO:", "Balanceada" if ok else "No Balanceada", "\n")

if __name__ == '__main__':
    main()
