def student(**stud):
    for s in stud:
        print(s + " : " + str(stud[s]))

student(age = 30, lastname = "Patel", firstname ="Fenil", m1=50,m2=60)