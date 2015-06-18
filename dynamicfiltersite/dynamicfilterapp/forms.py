from django import forms
from models import Restaurant, RestaurantPredicate, PredicateBranch

class WorkerForm(forms.Form):
    """
    sets up a form for the worker to answer questions
    """
    # choice fields for worker answering predicates
    WORKER_ANSWER_CHOICES = (
        (None, "------"),
        (True, 'Yes'),
        (False, 'No'),
    )

    # how confident a worker is in his/her answer
    CONFIDENCE_LEVELS = (
        (None, '------'),
        ('50', '50%'),
        ('60', '60%'),
        ('70', '70%'),
        ('80', '80%'),
        ('90', '90%'),
        ('100', '100%'),
    )

    # sets up form for answering predicate and worker's confidence level
    answerToQuestion = forms.ChoiceField(choices=WORKER_ANSWER_CHOICES, 
        label='Your answer')
    confidenceLevel = forms.ChoiceField(choices=CONFIDENCE_LEVELS, 
        label='Confidence level')

class RestaurantAdminForm(forms.ModelForm):
    """
    sets up form for admin when adding in restaurants to database
    """
    class Meta:
        # Tells Django which model is being created and which fields to display
        model = Restaurant
        fields = ['name', 'url', 'text', 'street', 'city',
                'state', 'zipCode', 'country', 'predicate0Status',
                'predicate1Status', 'predicate2Status']

    def save(self, commit=True):
        # Save (create or update) the Restaurant generated by this form
        instance = super(RestaurantAdminForm, self).save(commit=False)
        fields = []
        numPredicates = instance.numOfPredicates
        for i in range(0,numPredicates):
            field.append("predicate_"+str(i))
        for field in fields:
            instance.add_to_class(field, models.IntegerField(default=5))
            
        instance.save()
        
        # Create the three associated predicates if they don't exist  yet
        RestaurantPredicate.objects.get_or_create(index=0, restaurant=instance, 
            question="Does this restaurant accept credit cards?")
        RestaurantPredicate.objects.get_or_create(index=1, restaurant=instance, 
            question="Is this a good restaurant for kids?")
        RestaurantPredicate.objects.get_or_create(index=2, restaurant=instance, 
            question="Does this restaurant serve Choco Pies?")
        
        # Create the three predicate branches if they don't exist yet
        for predicate in RestaurantPredicate.objects.all():
            PredicateBranch.objects.get_or_create(index=predicate.index, 
                question=predicate.question)

        return instance


class IDForm(forms.Form):
    """
    sets up form for worker to enter in his/her ID number
    """
    workerID = forms.IntegerField(label='Worker ID', min_value=0)