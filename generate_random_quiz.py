import csv
from random import shuffle
from html_generator import generate_html_file
import os
import pdfkit
from contextlib import contextmanager

def get_questions():
	with open("questions.txt", "r") as qfile:
		questions = [question.strip() for question in qfile]
	return questions

def get_answers():
	with open("correct_ans.txt", "r") as afile:
		answers = [answer for answer in afile]
	return answers

data_file = open("data.csv", "r")
students_data = list(csv.DictReader(data_file))

for data in students_data:
	with open("fake_ans.csv", "r") as fafile:
		questions = get_questions()
		options = csv.reader(fafile)
		questions_and_options = list(zip(questions, options))
		shuffle(questions_and_options)
		questions, options = zip(*questions_and_options)
		content = generate_html_file(data, questions, options)

	with open(f"tests/quiz_roll_no_{data['RollNo']}.html", "w") as new_file:
		new_file.write(content)

# creating custom contextmanager for generating pdf from
# HTML files and delete all HTML files after conversion.
@contextmanager
def read_dir(destination):
	cwd = os.getcwd()
	os.chdir(destination)
	files = [file for file in os.listdir()]
	yield files
	# now delete the HTML files from directory
	[os.remove(file) for file in files if file.endswith('.html')]
	os.chdir(cwd)

with read_dir('./tests/') as files:
	for file in files:
		# generate PDF file
		pdfkit.from_file(file, f"{file.split('.')[0]}.pdf")
