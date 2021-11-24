import cyk

def main():
    verdict = cyk.getVerdict(cyk.cyk())
    if verdict:
        print("Accepted")
    else:
        print("Syntax Error")
main()