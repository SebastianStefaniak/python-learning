dictionary = {'Sebastian' : 85,
              'Alice' : 95,
              'Bob' : 52,
              'Marek' : 65
}
total=0
for name,points in dictionary.items():
    total+=points
    if points >90:
        print(name,"A")
    elif points >= 75 and points <= 89:
        print(name, "B")
    elif points >= 60 and points <= 74:
        print(name, "C")
    else:
        print(name, "F")
average=total/len(dictionary)
print('Average score is', average)

