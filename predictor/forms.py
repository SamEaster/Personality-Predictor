# predictor/forms.py

from django import forms

class PersonalityForm(forms.Form):
    """A form to capture personality trait inputs."""
    
    # Define fields with validation rules
    Time_spent_Alone = forms.IntegerField(
        label="Time Spent Alone", 
        min_value=0, 
        max_value=8,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-8'
        })
    )
    Stage_fear = forms.IntegerField(
        label="Stage Fear", 
        min_value=0, 
        max_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-1'
        })
    )
    Social_event_attendance = forms.IntegerField(
        label="Social Event Attendance", 
        min_value=0, 
        max_value=8,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-8'
        })
    )
    Going_outside = forms.IntegerField(
        label="Going Outside", 
        min_value=0, 
        max_value=8,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-8'
        })
    )
    Drained_after_socializing = forms.IntegerField(
        label="Drained After Socializing", 
        min_value=0, 
        max_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-1'
        })
    )
    Friends_circle_size = forms.IntegerField(
        label="Friends Circle Size", 
        min_value=0, 
        max_value=8,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-8'
        })
    )
    Post_frequency = forms.IntegerField(
        label="Social Media Post Frequency", 
        min_value=0, 
        max_value=8,
        widget=forms.NumberInput(attrs={
            'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Enter value 0-8'
        })
    )