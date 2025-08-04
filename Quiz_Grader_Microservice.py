import zmq

#Define the context and the socket for ZeroMQ communication
my_context = zmq.Context()

grader_socket = my_context.socket(zmq.REP)

grader_socket.bind("tcp://*:1111")

def calc_letter_grade(percentage):
    """A function that determines a grade from a given percentage."""
    if percentage < 60:
        return "F"
    if  70 > percentage >= 60:
        return "D"
    if 80 > percentage >= 70:
        return "C"
    if 90 > percentage >= 80:
        return "B"
    if 100 >= percentage >= 90:
        return "A"

print("Starting the Grading service!")

#Define last quiz as none, for conditional functionality with showing last quiz data in the result.

last_quiz = None

#Initiate UI menu loop

while True:

    #Define a variable first_int to receive the first string from the client - the total number of questions

    first_int = grader_socket.recv()

    print(f"Received total_questions integer string from the Client: {first_int.decode()}")
    total_questions = int(first_int)

    #Define a send a helpful confirmation string to the client, to inform them that the first message was received.
    confirmation_string = str("Total questions received, send number of correct")

    grader_socket.send_string(confirmation_string)
    print("The Message: " + confirmation_string)
    print("was successfully sent to the client.")


    #Define a variable second int to receive the second string from the client - the total number of questions correct.

    second_int = grader_socket.recv()
    print(f"Number correct received from the client : {second_int.decode()}")
    number_correct = int(second_int)

    #Calculate a percentage score, and then define grade as a call calc_letter_grade with the percentage score as a parameter, to get the letter grade.

    integer_grade = (number_correct / total_questions) * 100

    grade = calc_letter_grade(integer_grade)


    #Define the percentage grade score as a string, to get ready to send it as a message.
    grade_string = str(integer_grade)

    #Define conditional statement - if the last quiz data exists, include it in the report, if not, then only report on the current quiz.
    if last_quiz is not None:
        last_grade = calc_letter_grade(float(last_quiz))
        grade_report = "Your current score is " + str(number_correct) + " / " + str(total_questions) + ". Which is " + grade_string + "%. " + "You got a grade of " + grade +   ". Your last score was " + last_quiz + "%. Your last grade was " + last_grade + "."
        grader_socket.send_string(grade_report)
    else:
        grade_report = "Your current score is " + str(number_correct) + " / " + str(total_questions) + ". Which is " + grade_string + "%. You got a grade of " + grade + "."
        grader_socket.send_string(grade_report)
        print(f"Grade report sent to the client")

    #define last quiz, as the current percentage score.

    last_quiz = grade_string












