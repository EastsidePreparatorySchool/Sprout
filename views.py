from django.shortcuts import render, redirect
from .forms import SliderForm

def home(request):
    return render(request, 'leaf/home.html')

def slider_submit(request):
    if request.method == 'POST':
        form = SliderForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            return redirect('leaf:slider_result', value=value)
    else:
        form = SliderForm()
    return render(request, 'leaf/slider_submit.html', {'form': form})

def slider_result(request, value):
    return render(request, 'leaf/slider_result.html', {'value': value})
