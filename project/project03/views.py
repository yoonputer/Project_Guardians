from django.shortcuts import render
import pandas as pd
import numpy as np
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
	df = pd.read_excel('./ML/ML_i/test.xls')
	df = df.replace(np.nan, 'null')
	dates = df.date.dt.date.unique().tolist()
	date = []
	for i in dates:
		date.append(i.strftime('%Y-%m-%d %H:%M:%S'))
	raw = df.raw.values.tolist()
	lower = df.lower.values.tolist()
	upper = df.upper.values.tolist()
	mean = df['mean'].values.tolist()
	dateindex = pd.date_range(start='2/1/2007', end='10/1/2022', freq='MS')

	context = {
		'date':date,
		'dateindex':dateindex,
		'raw':raw,
		'lower':lower,
		'upper':upper,
		'mean':mean
	}
	return render(request, 'test.html', context)