def isvalid(s):
    if len(s)%2==0:
        closer=[]
        for i in s:
            if i =="{":
                closer.append("}")
            elif i =="[":
                closer.append("]")
            elif i =="(":
                closer.append(")")
            else:
                if i==closer[-1]:
                    closer.pop()
                else:
                    return "invalid"
        return "valid"
    else: 
        return "invalid"
if __name__ == "__main__":
    s="{()[{}]}[]"
    print(isvalid(s))