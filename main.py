import cyk

def main():
    verdict = cyk.getVerdict(cyk.cyk())
    if verdict:
        print("No syntax error detected")
    else:
        print("SyntaxError: invalid syntax")
main()