# This is the code that contains the stub functions that simulate API interface to external systems

# For Stubs
from datetime import datetime, timedelta

#----------------------------------- STUBS --------------------------------------------------
# For Demo or POC orchestrator, write stub functions as needed
# For production systems, these will be replaced with API calls to real systems

def stub_function(stub_args):
    global global_vars

    # Stub Code Here

# Stub for Get Appointment
# This accepts user's date / time if given; else next day 11 AM is given as appointment
# Replace this with appropriate API call to appointment system

def get_appointment (current_context, user_given_date, user_given_time):

    print ("In get_appointment") # For debugging
    print ("date", user_given_date, "time", user_given_time) # For debugging
    if user_given_date:
        current_context['appt_date'] = user_given_date
    else:
        current_context['appt_date'] = (datetime.today() + timedelta(1)).strftime('%d-%m-%Y')
    if user_given_time:
        current_context['appt_time'] = user_given_time
    else:
        current_context['appt_time'] = "11 AM"
    print("context date", current_context['appt_date'], "context time", current_context['appt_time']) # For debugging

# Stub for Confirm Appointment
# This confirms given date / time
# Replace this with appropriate API call to appointment system
def confirm_appointment (current_context, date, time):
    print ("In confirm_appointment") # For debugging
    current_context['appt_date'] = date
    current_context['appt_time'] = time

#--------------------------------------END STUBS --------------------------------------------

