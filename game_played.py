def played():
    n=6
    m=6
    games=[[1,6,3,4,5,2],[6,4,2,3,1,5],[4,2,1,5,6,3],[4,5,1,6,2,3],[3,2,5,1,6,4],[2,3,6,4,1,5]]
    p=n*(n-1)
# print(int(p/2))
    played=[]
    for i in games:
        # print(i)
        team_x = i[0:int(n/2)]
        team_y = i[int(n/2):n]
        print(team_x)
        print(team_y)
        for x in team_x:
            for y in team_y:

                if y > x:
                    if str(y)+str(x) not in played:
                        played.append(str(y)+str(x))
    print(played)
    if len(played) == int(p/2):
        return True
    else:
        return False
print(played())


                
