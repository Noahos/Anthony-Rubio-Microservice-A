import zmq

#define the context for zeromq
my_context = zmq.Context()



def grade_quiz(number_correct, total_questions):
    """A function that takes the total number of questions, and number of questions correct as parameters,
    and places a call to the quiz grading microservice, to get the quiz data graded. It will return a written report
    with the quiz grade"""

    print("Client sending first integer string to the server....")

    #Define the socket for zeromq, and then connect to the port address
    my_socket = my_context.socket(zmq.REQ)

    my_socket.connect("tcp://localhost:1111")

    #convert the integers of correct questions, and total questions, to strings, to send through zero

    print("Sending the first integer with message string...")

    str_correct = str(number_correct)
    str_questions = str(total_questions)


    #send the number of questions using zeromq first.
    my_socket.send_string(str_questions)


    #Use the receive method to wait for the confirmation message from the microservice
    my_message = my_socket.recv()

    print(f"Message Received : {my_message.decode()}")

    #send the number of correct questions to the microservice
    print("Sending the second integer with message string")

    my_socket.send_string(str_correct)

    #Receive my quiz grade report from the quiz grading microservice

    my_grade = my_socket.recv()

    print(f"Grade Received : {my_grade.decode()}")

    return my_grade.decode()

#While loop that launches a cyclical user interface, allowing the user to define variables to call as parameters in the grading function.
while True:
    number_questions = input("Enter the total number of questions on the quiz: ")
    correct_questions = input("Enter the number of questions correct: ")

    grade_quiz(correct_questions,number_questions)



