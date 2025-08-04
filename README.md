# Anthony-Rubio-Microservice-A
A microservice for Anthony Rubio's flashcard program, that takes in quiz data, and returns results, letter grade, and comparison to the last quiz results.

## 1. Clear instructions for how to programmatically **REQUEST** data from the microservice with an example call

The following is an example of how to call the microservice.  
In this example, the program prompts the user to enter integers to define variables.  
In the actual main program, quiz data will likely be preloaded, and the program will call a function that activates the microservice directly.

Environment:
- install **zeromq** in python
- import zmq
  
Run both:
- The **microservice** file  
- Your **main program** on your local system  

The main program will prompt you to enter:
- The total number of questions on the quiz  
- The number of questions answered correctly  

Once those variables are defined, the program calls the function:

```python
grade_quiz(number_correct, total_questions)
```

This initiates communication with the microservice grading process.

---

### Communication Protocol
The communication protocol used is **ZeroMQ**.  

Define a socket and choose a local port. For example:

```python
my_socket = my_context.socket(zmq.REQ)
my_socket.connect("tcp://localhost:1111")
```

---

### Sending Data to the Microservice

First, define the quiz data:

```python
str_correct = str(number_correct)
str_questions = str(total_questions)
```

**Send the total number of questions possible first:**

```python
my_socket.send_string(str_questions)
my_message = my_socket.recv()
print(f"Message Received : {my_message.decode()}")
```

The microservice will send back a confirmation message that the first string was received.

---

**Now send the number of correct questions:**

```python
print("Sending the number of correct questions with message string")
my_socket.send_string(str_correct)
```

---

## 2. Clear instructions for how to programmatically **RECEIVE** data from the microservice with an example call

Once the second integer is sent to the microservice, it will send back the graded quiz data.

Prepare to receive the graded quiz:

```python
my_grade = my_socket.recv()
print(f"Grade Received : {my_grade.decode()}")
```

If the process executes seamlessly, 
The graded quiz data will now available in your main program.

- Example Output: "Grade Received : Your current score is 17 / 20. Which is 85.0%. You got a grade of B. Your last score was 90.0%. Your last grade was A."
- or if there is no previous quiz data: "Grade Received : Your current score is 18 / 20. Which is 90.0%. You got a grade of A."

---

## 3. UML Sequence Diagram

Below is a **UML sequence diagram** showing the request and response process.  

<img width="581" height="398" alt="image" src="https://github.com/user-attachments/assets/15fbe3b9-b584-4147-9ab3-a220602c45b8" />




