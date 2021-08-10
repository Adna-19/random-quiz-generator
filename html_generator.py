import csv
from yattag import Doc
from bs4 import BeautifulSoup
from random import shuffle

def generate_html_file(student, questions, options):
    """ Function for generating HTML files for given data."""
    doc, tag, text = Doc().tagtext()
    question_f = "Q{}:{}?"

    doc.asis('<!DOCTYPE html>')
    with tag('head'):
        doc.stag('link', href="../design.css", type="text/css", rel="stylesheet")
    with tag('body'):
        with tag('h1', id="page-header"):
            text("Quiz for Students")

        with tag('div', Class="students-info-banner"):
            with tag('h3'):
                text('Student\'s data:')
            doc.stag('br')
            with tag('ul', Class='students-info'):
                for key, value in student.items():
                    with tag('li'):
                        text('{}:{}'.format(key, value))
        # create some line breaks and horizontal line...
        doc.stag('br')
        doc.stag('hr')
        doc.stag('br')

        with tag('div', Class="questions-portion"):
            q_no = 1
            for question, option_set in zip(questions, options):
                shuffle(option_set)
                with tag('p', Class="question"):
                    text(question_f.format(q_no, question))
                options_no = ['a:', 'b:', 'c:', 'd:']
                with tag('p', Class='options'):
                    for option, option_no in zip(option_set, options_no) :
                        with tag('label', For=option):
                            text(option_no)
                            doc.stag('input', type='radio', name='option', value=option)
                            text(option)
                q_no += 1
                doc.stag('br')
                doc.stag('br')

    content = BeautifulSoup(doc.getvalue(), 'html.parser')
    return content.prettify()