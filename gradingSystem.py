#This is a Grading system for the Innovation Univaersity of Australia.
#Programmer: Vismini Beddewela

#Define the main() function.
def main():
    print('\n'+'-------------------------------------------------------------------')
    print('-------------------------------------------------------------------')
    #Ask user to select the routine that he wants to continue. 
    print("Welcome to the AGoS System of IUA"+'\n')
    print("Please select an option from the following.")
    print("<A>dd details of a student.")
    print("<S>earch student details for a student.")
    print("<Q>uit."+'\n')
    result=input("Enter the letter:")
    print('-------------------------------------------------------------------')
    print('-------------------------------------------------------------------'+'\n')

    #This if function is used to call the relevant function according to the user's selection.
    if result=='a'or result=='A':
        #Call the addStuDetails function.
        addStuDetails()
    elif result=='s' or result=='S':
        #Call the search function.
        searchStuDetails()
    elif result=='q' or result=='Q':
        #This would close the runing program. 
        return
        

#define the addStuDetails function.
def addStuDetails():
    print('\n'+'-------------------------------------------------------------------')
    print("The Innovation University of Australia (IUA) Grade System")
    print('-------------------------------------------------------------------')
    print("Please enter all marks out of 100."+'\n')

    #Ask detaails about the student form the user.
    stuId = input("Please enter the Student ID:"+'\t')
    stuName = input("Please enter thr Student Name:"+'\t')
    assignment_1=int(input("Please enter marks for Assignment 1:"+"\t"))
    assignment_2=int(input("Please enter marks for Assignment 2:"+"\t"))
    finalExam=int(input("Please enter marks for the Final Exam:"+"\t"))

    print("\n"+"Thank You!"+"\n")

    #Call the calMarks function.
    totWeightMark,totWeightWithBonus=calMarks(assignment_1,assignment_2,finalExam)

    #Write data into the IUA text file.

    #open the file.
    resultFile = open("IUA.txt",'a')

    #write the data into the file.
    resultFile.write('\n'+stuId+'\t'+'\t')
    resultFile.write(stuName+'\t')
    resultFile.write(str(assignment_1)+'\t')
    resultFile.write(str(assignment_2)+'\t')
    resultFile.write(str(finalExam)+'\t')
    resultFile.write(str(totWeightMark)+'\t'+'\t')
    resultFile.write(str(totWeightWithBonus))
    
    #close the file.
    resultFile.close()

    
    #Ask user whether he need to continune the proccess or not
    result2=input('\n'+"Do you want to enter marks for another Student (Y/N)?")
    
    if result2=='Y':
        addStuDetails()
    elif result2=='N':
        main()
    else:
        print('\n'+"You have entered a wrong letter")
        


#Define the calMarks function.
def calMarks(a1,a2,finalExam):
    #Assignment 1 posses 20% and follwoing is the process which calculate the assignment 1 weighted mark.
    weightedMark_1=a1*20/100

    #Assignment 2 posses 30% and follwoing is the process which calculate weighted mark for assignement 2.
    weightedMark_2=a2*30/100

    #Final exam posses 50% and follwoing is the process which calculate weighted mark for final exam.
    weightedMark_3=finalExam*50/100

    #This displays the weighted marks for the assignment 1 & 2.
    print("\n"+"Weighted mark for Assignment 1:"+"\t",weightedMark_1)
    print("Weighted mark for Assignment 2:"+"\t",weightedMark_2)
    
    #Total of the weighted mark for assignment 1 and 2. 
    totWeightMarkAssig = weightedMark_1 + weightedMark_2
    print("Total weighted mark for the Assignments:",totWeightMarkAssig)


    #This displays the weighted for the final exam.
    print("\n"+"Weighted mark for Final Exam:"+"\t",weightedMark_3)

    #This process use to calculate the total of the subject by adding the final exam weighted mark and assignments weighted mark. 
    totWeightMarkSubject = totWeightMarkAssig+weightedMark_3
    
    #This displays the total final weighted mark for the subject. 
    print("Total weighted mark for Subject:",totWeightMarkSubject)

    #Calculation of bonus mark
    if(totWeightMarkSubject>90): 
        bonusMark=5+2.0             
    elif(totWeightMarkSubject>70):
        bonusMark=2+1.5
    elif (totWeightMarkSubject>50):
        bonusMark=1.0
    else:
        bonusMark=0

    #Print the calculated bonus mark
    print("\n"+"Bonus Mark:",bonusMark)

    #Calculate the total subject mark with the bonus mark
    totMarkSubject=totWeightMarkSubject+bonusMark

    #if the total subject mark with bonus is greater than 100, then the total mark is reset to 100
    if(totMarkSubject>100):
        totMarkSubject=100
        print("Total mark with bonus:",totMarkSubject)
    else:
        print("Total mark with bonus:",totMarkSubject)

    return totWeightMarkSubject,totMarkSubject;


#Define the search function.
def searchStuDetails():
    #Ask student id from he user to search student details.
    stuId = input('\n'+"Please enter the Student ID:"+'\t')
    print('\n')
    #Open the text file in read only mode.
    readFile = open("IUA.txt",'r')

    #Create an empty list
    lineList = []

    #initialize the variable i
    i=0

    #for loop is to read the file line by line while appending the line to list
    for line in readFile:
        lineList.append(line.rstrip('\n'))

        #if condition checks the matching list index with the student id
        if stuId in lineList[i]:
            print("Student"+'\t'+'\t'+"Student"+'\t'+'\t'+"A1"+'\t'+"A2"+'\t'+"Final"+'\t'+"Weighted"+'\t'+"Weighted Total")
            print("Id"+'\t'+'\t'+"Name"+'\t'+'\t'+'\t'+'\t'+"Exam"+'\t'+"Total"+'\t'+'\t'+"with Bonus")
            print("----------------------------------------------------------------------------------"+'\n')
            print(lineList[i]) #print the searched result
            break; #stops the for loop
        else:
            i+=1

    #Ask user for further process
    result3=input('\n'+"Do you want to search for another Student (Y/N)?")
    
    if result3=='Y':
        searchStuDetails()
    elif result3=='N':
        main()
    else:
        print('\n'+"You have entered a wrong letter")

#Call the main() function.
main()
