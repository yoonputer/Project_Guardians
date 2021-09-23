from django.shortcuts import render
import pandas as pd
import numpy as np
import sqlite3
# Create your views here.

def index(request):

	return render(request, 'index.html')
def blog(request):

	return render(request, 'blog.html')
def elements(request):

	return render(request, 'elements.html')
def blog_details(request):

	return render(request, 'blog_details.html')

def test(request):
	# industry = request.GET.get('industry')
	# place = request.GET.gt('place')
	# in_pl = str(industry) + str(place)
	in_pl = 'building강원도'
	db_test = sqlite3.connect('./timeseries.db')
	c = db_test.cursor()
	df = pd.read_sql("SELECT * FROM "+in_pl+"", db_test, index_col=None)
	# df = pd.read_excel('./ML/ML_i/test.xls')
	# df = pd.read_excel('./ML/ML_i/sample.xls')
	df = df.replace(np.nan, 'null')
	date = df.date.tolist()
	raw = df.raw.values.tolist()
	lower = df.lower.values.tolist()
	upper = df.upper.values.tolist()
	mean = df['mean'].values.tolist()

	context = {
		'date':date,
		'raw':raw,
		'lower':lower,
		'upper':upper,
		'mean':mean
	}
	return render(request, 'test.html', context)