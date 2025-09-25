# predictor/views.py

import joblib
import numpy as np
from django.shortcuts import render
from django.conf import settings
import os
from .forms import PersonalityForm

# Construct the path to the model and load it once when the app starts
MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor', 'static', 'predictor', 'model.pkl')
model = joblib.load(MODEL_PATH)

def predict_personality(request):
    """
    Handles GET and POST requests.
    GET: Displays the empty form.
    POST: Processes form data, predicts personality, and displays the result.
    """
    result = None
    form = PersonalityForm() # Initialize the form

    if request.method == 'POST':
        form = PersonalityForm(request.POST)
        if form.is_valid():
            # Extract data from the validated form
            data = form.cleaned_data
            
            # Prepare data for the model
            input_data = np.array([list(data.values())]).reshape(1, -1)
            
            # Make prediction
            prediction = model.predict(input_data)
            
            # Interpret the result
            result = 'Introvert' if prediction[0] == 1 else 'Extrovert'

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'predictor/index.html', context)