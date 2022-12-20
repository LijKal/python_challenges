def callpoint(rule):
    records=[]
    for i in rule:
        if i =="+":
            records.append(records[-1]+records[-2])
        elif i =="D":
            records.append(2*records[-1])
        elif i =="C":
            records.pop()
        else:
            records.append(int(i))
    return sum(records)
if __name__ == "__main__":
    rule=["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(callpoint(rule))