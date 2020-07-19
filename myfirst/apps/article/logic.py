def SplitAndGive(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
    print("% of lower: ", (d["LOWER_CASE"]/len(s))*100)
    print("% of upper: ", (d["UPPER_CASE"]/len(s))*100)
    lower = str((d["LOWER_CASE"]/len(s))*100)
    upper = str((d["UPPER_CASE"]/len(s))*100)
    return lower, upper, s


if __name__ == '__main__':
	SplitAndGive(input('enter string: '))