try:
    from data import menu
except:
    import traceback
    import sys
    f = open("traceback.txt", "w")
    print("I'm sorry but an error has found while executing your script", file=f)
    print("in \"script.py\" location folder.", file=f)
    print(file=f)
    traceback.print_exc(None, f)
    print(file=f)
    print("----- Full Traceback ------------------------------", file=f)
    type, value, tb = sys.exc_info()
    traceback.print_tb(tb, None, f)
    traceback.print_tb(tb, None, sys.stdout)
    sys.exit(-1)
