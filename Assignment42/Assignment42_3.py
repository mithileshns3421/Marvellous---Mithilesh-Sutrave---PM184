import math

def Euc(p1,p2):
    Ans = math.sqrt((p1["Study Hours"]-p2["Study Hours"])**2+(p1["Attendance"]-p2["Attendance"])**2)
    return Ans 

def Userdefined(NX,NY):
    border="*"*90
    Data=[
        {"Study Hours":2,"Attendance":60,"Result":"Fail"},
        {"Study Hours":5,"Attendance":80,"Result":"Pass"},
        {"Study Hours":6,"Attendance":85,"Result":"Pass"},
        {"Study Hours":1,"Attendance":50,"Result":"Fail"}


    ]
    print(border)
    print("\nThe Data is : \n")
    for i in Data :
        print(i)
    print(border)
    
    new_point={"Study Hours":NX,"Attendance":NY}
    for d in Data:
        d["distance"]=Euc(d,new_point)
    print(border)

    print("\nData with distance is : \n")
    for i in Data:
        print(i)
    print(border)

    sorted_data=sorted(Data , key=lambda item : item["distance"])
    print("\nSorted data is : \n")
    for i in sorted_data:
        print(i)
    print(border)

    sorted_data=sorted_data[:3]

    votes={}
    for d in sorted_data:
        label=d["Result"]
        votes[label]=votes.get(label,0)+1
    print(border)

    print("\nResulting votes are :",votes)
    print()
    print(border)

    a=0
    name='' 
    for d in votes:
        if(votes[d]>a):
            a=votes[d]
            name=d
    print("\nFinal prediction is : ",name)
    print()
    print(border)


def main():
    x=int(input("\nEnter Study Hour : "))
    y=int(input("\nEnter Attendance :"))
    Userdefined(x,y)


if __name__=="__main__":
    main()