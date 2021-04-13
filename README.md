# Stack-Overflow-Auto-Search-Tool
A Crio.do project (Reference for the code = Geeksforgeeks.org)
The project consists of -
 1. A python code with incorrect input.
 2. A wrapper script which takes our python code as input and then performs the following operations:
    a. Checks for errors (if errors exist then extracts and filters the error message).
    b. If error exists in our code then executes the stackexchange api to open respective Stackoverflow threads for that particular error.
    c. Else prints "No errors found".
 
 Concepts :
  1. Python - Use of Python modules like subprocess , urllink.requests , webbrowser.
  2. Shallow understanding of HTTP and Rest APIs.(as we are passing the type of file(python) as "tagged",and the error message and type as "intitle" and in return getting the     links for the respective Stack Overflow threads as JSON(Javascript Object Notation).
  
 Overview :
 
 What is Stack Overflow?
 - Stack Overflow is a source of helpful information for software development-related queries.
 
 Important Links for the project(Sources):-
 1. https://api.stackexchange.com/docs
 2. https://www.geeksforgeeks.org/python-traceback/
 3. https://docs.python.org/3/library/subprocess.html
 4. https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python
 5. https://www.geeksforgeeks.org/get-post-requests-using-python/
 6. https://docs.python.org/3.8/library/webbrowser.html
 
 
 Glimpses of the project :
 
 The incorrect source code :
 
 ![image](https://user-images.githubusercontent.com/71055951/114496413-84ce9000-9c3d-11eb-91c8-5dee39eb2379.png)
 
 Wrapper Python Script :
 
 ![image](https://user-images.githubusercontent.com/71055951/114496518-c0695a00-9c3d-11eb-8d4f-49ddf4c016c9.png)

Output of Wrapper Script(or the stackexchange api) :

![image](https://user-images.githubusercontent.com/71055951/114496790-54d3bc80-9c3e-11eb-9d0d-6bfdf9d61a4e.png)

Stackoverflow threads we got :

![image](https://user-images.githubusercontent.com/71055951/114497324-7c775480-9c3f-11eb-87f1-55721c3581bb.png)


 
 

