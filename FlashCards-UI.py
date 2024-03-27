try:
    import tkinter as tk
    import random
    import os
    import datetime
except ImportError as e:
    print(f"Error: {e}")
    print("Please make sure all required libraries are installed.")
    input()

Icon = "Icon"
if os.path.exists(Icon):
    print("'Icon' folder already exists")
else:
    print("Creating Icon folder")
    os.makedirs(Icon)
    print("'Icon' folder created")

import urllib.request

def download_file(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"File downloaded successfully to: {save_path}")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")


ico_url = "https://raw.githubusercontent.com/Bernso/Icons/main/Dead.ico"
save_path = os.path.join(Icon, "Dead.ico")  # Full file path including directory
download_file(ico_url, save_path)



app = tk.Tk()
app.geometry('500x225')
app.title("Revision Cards by Bernso")
app.iconbitmap("Icon/Dead.ico")




words = [
    "Abstraction",
    "Algorithm",
    "API (Application Programming Interface)",
    "Array",
    "ASCII (American Standard Code for Information Interchange)",
    "Boolean",
    "Bug",
    "Byte",
    "Code",
    "Compiler",
    "CPU (Central Processing Unit)",
    "Data",
    "Debugging",
    "Encryption",
    "Function",
    "GUI (Graphical User Interface)",
    "Hardware",
    "HTTP (Hypertext Transfer Protocol)",
    "IDE (Integrated Development Environment)",
    "Input",
    "Integer",
    "Internet",
    "Loop",
    "Memory",
    "Object",
    "Output",
    "Program",
    "Protocol",
    "Python",
    "RAM (Random Access Memory)",
    "Recursion",
    "Script",
    "Software",
    "Syntax",
    "TCP/IP (Transmission Control Protocol/Internet Protocol)",
    "URL (Uniform Resource Locator)",
    "Variable",
    "WWW (World Wide Web)"
]

definitions = [
    "The process of representing complex real-world systems with simplified models.",
    "A precise set of instructions for solving a specific problem or accomplishing a particular task.",
    "A set of rules and protocols that allows different software applications to communicate with each other.",
    "A data structure that stores a collection of elements, typically of the same type, in contiguous memory locations.",
    "A character encoding standard that represents text characters using integers.",
    "A data type that can have one of two values: true or false.",
    "An error or flaw in a computer program that causes it to produce incorrect or unexpected results.",
    "A unit of digital information that consists of 8 bits.",
    "Instructions written in a programming language that tell a computer what to do.",
    "A program that translates source code written in a high-level programming language into machine code.",
    "The electronic circuitry within a computer that carries out the instructions of a computer program.",
    "Facts, figures, or instructions processed by a computer.",
    "The process of identifying and fixing errors or defects in a computer program.",
    "The process of converting plaintext into ciphertext to secure it from unauthorized access.",
    "A named section of a program that performs a specific task.",
    "A type of user interface that allows users to interact with electronic devices through graphical icons and visual indicators.",
    "The physical components of a computer system, including the processor, memory, and input/output devices.",
    "The protocol used for transferring hypertext requests and information over the internet.",
    "A software application that provides comprehensive facilities to computer programmers for software development.",
    "Data provided to a computer or program for processing.",
    "A whole number, either positive, negative, or zero.",
    "A global network that connects millions of computers worldwide, facilitating communication and information exchange.",
    "A programming construct that repeats a set of instructions until a specific condition is met.",
    "The part of a computer in which data and instructions are stored temporarily during program execution.",
    "An instance of a class in object-oriented programming that encapsulates data and methods.",
    "Data produced as a result of executing a computer program.",
    "A set of instructions that tells a computer what tasks to perform.",
    "A set of rules and conventions governing the structure and format of programming languages.",
    "A high-level programming language known for its simplicity and ease of use.",
    "A type of computer memory that allows data to be accessed randomly, rather than sequentially.",
    "A programming technique in which a function calls itself.",
    "A series of instructions written in a scripting language that are executed by an interpreter or scripting engine.",
    "A collection of programs, data, and instructions that enable a computer to perform specific tasks.",
    "The set of rules and conventions that govern the syntax and semantics of a programming language.",
    "A set of communication protocols used to transmit data over networks, including the internet.",
    "The address used to identify resources on the World Wide Web.",
    "A named storage location in a computer's memory that can hold different values during program execution.",
    "A system of interlinked hypertext documents accessed via the internet."
]



showing_definition = True
last_shown_index = None
current_index = None
times_ran = 0

def swap_cards():
    global showing_definition, last_shown_index, current_index, times_ran
    
    if times_ran % 2 == 0:
        current_index = random.randint(0, len(words) - 1)
        while current_index == last_shown_index:
            current_index = random.randint(0, len(words) - 1)
            
    if showing_definition:
        try:
            last_shown_index = current_index
            start_label.configure(text=f"Hint: \n{definitions[current_index]}") # type: ignore
            flip_button.configure(text="Flip")
            
        except Exception as e:
            print("An error occurred:", e)
            
    else:
        if last_shown_index is not None:
            start_label.configure(text=f"Word: \n{words[last_shown_index]}")
            flip_button.configure(text="Next")
            
    showing_definition = not showing_definition
    times_ran += 1

def quitv2():
    try:
        revision_count = int(times_ran / 2)
        if revision_count == 1:
            print(f"\nYou completed a singular revision card")
        elif revision_count == 0:
            print("\nBro did no revision cards 💀\nWhy did you even run the program?")
        else: 
            print(f"\nYou completed {revision_count} revision card(s)")
        
        # current date and time
        current_datetime = datetime.datetime.now()
        
        # Format the date and time as a string
        timestamp = current_datetime.strftime("%Y-%m-%d__%H-%M-%S")
        
        # Create the logs directory if it doesn't exist
        if not os.path.exists("logs"):
            try:
                print("\nCreating 'logs' directory")
                os.makedirs("logs")
                
            except Exception as e:
                print(f"Error creating logs directory: {e}")
        else:
            print("\nLogs directory already exists")
            
        # Create the file path
        file_path = os.path.join("logs", f"{timestamp}.txt")
        
        # Write the revision count to the file
        try:
            with open(file_path, "w") as file:
                file.write(f"Revision cards completed: {revision_count}")
            print("Logs saved")
        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"An error occured:\n{e}")
    quit()
    
start_label = tk.Label(app, text="Definitions and Answers will show:\nHERE", font=("Arial", 14, "bold"), wraplength=400, justify="center")
start_label.pack(padx=10, pady=10)

exit_button = tk.Button(app,
                        text="Exit",
                        command=quitv2,
                        bg='red',
                        fg='white',
                        font=('Arial'),
                        width=10,
                        height=1,
                        borderwidth=3,
                        relief='groove',
                        highlightthickness=0) 
exit_button.pack(side='bottom', padx=10, pady=10)

flip_button = tk.Button(app,
                        text="Start",
                        command=swap_cards,
                        bg='green',
                        fg='white',
                        font=('Arial'),
                        width=10,
                        height=1,
                        borderwidth=3,
                        relief='groove',
                        highlightthickness=0)
flip_button.pack(side='bottom', padx=5, pady=5)





app.mainloop()