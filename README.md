# random-quiz-generator

I got this assignment during my python classes. 
The task was to write a python script which can generate random quizzes in 
the form of .PDF files. Generally it consists of two code files.

 - generate_random_quiz.py
  which is the initalization step, the execution starts from this file. 
this file reads data from csv files i.e students data and questions/answers.

 - html_generator 
 this file generates html file for each quiz paper. The approach I took was 
to first generate an html file for a quiz paper and then transform that html
file to pdf. At that time this was the easy step for me.

 - For PDF generation I have used the Yattag (python package). I know there
are a lot more, but at that time this was the first package I got aftering searching.

There are some sample test files in tests directory generated from
this script.
