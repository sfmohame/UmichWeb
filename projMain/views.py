from flask import render_template, request
from app import app
from schedule_api import get_terms
from schedule_api import get_schools
from schedule_api import get_subjects
from schedule_api import get_classes
from schedule_api import get_courseD
from schedule_api import get_sections
from schedule_api import get_classNums

@app.route('/')
def index():
    options = {}
    try:
        options['terms'] = get_terms()
    except:
        options['api_error'] = True

    return render_template('index.html', **options)



@app.route('/aboutus')
def aboutuspage():

	return render_template('aboutUs.html')

@app.route('/services')
def servicespage():

    return render_template('services.html')

@app.route('/contact')
def contactpage():

    return render_template('contact.html')

@app.route('/schools/<termcode>')
def schoolpage(termcode):
    options = {}
    options['termcode'] = termcode
    try:
        options['schools'] = get_schools(termcode)
    except:
        options['api_error'] = True

    return render_template('schools.html', **options)

@app.route('/schools/<termcode>/subject/<sub>')
def subjectpage(termcode, sub):
    options = {}
    options['termcode'] = termcode
    options['sub'] = sub
    try:
        options['subjects'] = get_subjects(termcode, sub)
    except:
        options['api_error'] = True

    return render_template('subjects.html', **options)

@app.route('/schools/<termcode>/subject/<sub>/<subSelected>')
def classpage(termcode, sub, subSelected):
    options = {}
    options['termcode'] = termcode
    options['sub'] = sub
    options['subSelected'] = subSelected
    try:
        options['classes'] = get_classes(termcode, sub, subSelected)
    except:
        options['api_error'] = True

    return render_template('classes.html', **options)

@app.route('/schools/<termcode>/subject/<sub>/<subSelected>/<catNum>')
def classinfo(termcode, sub, subSelected, catNum):
    options = {}
    options['termcode'] = termcode
    options['sub'] = sub
    options['subSelected'] = subSelected
    options['catNum'] = catNum
    try:
        options['CourseDescr'] = get_courseD(termcode, sub, subSelected, catNum)
        options['sections'] = get_sections(termcode, sub, subSelected, catNum)
        options['SearchResults'] = get_classNums(termcode, subSelected,catNum)
    except:
        options['api_error'] = True

    return render_template('classinfo.html', **options)







