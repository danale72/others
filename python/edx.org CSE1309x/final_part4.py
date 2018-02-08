#Write a function named my_final_grade_calculation that receives a file name and returns a dictionary that tells whether a student in this
#course passed or failed based on the following criteria. 
#
#Each line of the file will have the format:
#
#name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final
#where
#name is a string
#q1 through q6 are quiz scores (integers)
#a1 through a4 are assignment scores (integers values)
#midterm is midterm score (integer)
#final is final exam score (integer)
#For example, if the content of the file looks like this:
#tom, 10, 20, 0, 100, 0 , 100,      70, 80, 90,   0,    80, 85
#mary, 0, 50, 66, 40, 10,  60,      70, 80, 90, 100,    80, 85
#joan, 0, 80, 40, 10, 50,  60,       7, 80, 90,   0,    80,  5
#Note that there may be additional spaces between the entries in each line. 

#Your function should return a dictionary such as:
#{"tom":"pass", "mary":"pass", "joan":"fail"} 
#Notes:
#Two of the lowest quizzes should be dropped and the average of the remaining four quizzes is worth 25% of the total grade.
#The lowest assignment score should be dropped and the average of the remaining three assignments is worth 25% of the total grade.
#Midterm and final exams are each 25% of the total grade.
#Calculate the total score of the student and if the total score is greater than or equal to 60 (totalscore >= 60) then the student
# has passed. Notice that the keys (names) and the values (pass or fail) of the dictionary should be all lower cased with no spaces in any of them.
def my_final_grade_calculation(filename) :
    # helper function for average
    def average(my_list):
        listsum = 0;
        for item in my_list:
            listsum += int(item)
        return listsum/len(my_list)

    result = {}
    try:
        datafile = open(filename, "r")
    except:
        print("Error openting", filename)
    else:
        result = {}
        # actual code of the app
        lines = datafile.readlines()
        for line in lines :
            if (line[0] == "#") :
                continue
            line = line.replace("\n","")
            values = line.split(",")
            for i in range(1,len(values)) :
                values[i] = int(values[i])

            
            # split list into logical part of the grades
            quizzes = values[1:7]
            assignment = values[7:11]
            quizzes.sort()
            assignment.sort()

            midterm = values[11]
            finalterm = values[12]

            avgQuizz = average(quizzes[2:])
            avgAssignment = average(assignment[1:])

            total = (avgQuizz + avgAssignment + midterm + finalterm) * 0.25
            #print(assignment[1:])

            if (total >= 60) :
                result[values[0].lower()] = "pass"
            else:
                result[values[0].lower()] = "fail"
    return result

print(my_final_grade_calculation("final4_test_data.txt"))
