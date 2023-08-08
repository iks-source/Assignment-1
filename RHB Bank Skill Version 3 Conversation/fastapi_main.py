# This is the code that contains the Webhook's FastAPI routes, and starts upthe FastAPI app
# It imports the stubs and webhook main files

# import webhook_main code
import webhook_main
from webhook_main import context_table, process_response, get_next_question, process_conversation_end, intent_table, context_table
from dbaccess import load_intent_table, open_response_db
# import Dataframe
import pandas as pd
# import FastAPI
from fastapi import FastAPI, Request
from importlib import reload

# This is a FastAPI App
app = FastAPI(debug=True)

# Webhook Routes
@app.get('/')
def hello_world():
    return 'Hello world!'

# **** Replace templatev3 with a unique bot name
@app.post('/beso/RHBv3/watsonwebhook')
async def watsonwebhook(request: Request):

    global context_table

    # Parse the request received from chatbot
    bot_input = await request.json()

    print("bot_input", bot_input) # For debugging

    # Get the intent and session ID from chatbot input
    intent = bot_input["intent"]
    session_id = bot_input["session_id"]

    # Depending upon the intent, the processing will differ

    # At end of conversation, store all details into database and delete the context
    if intent == 'End':
        bot_resp = process_conversation_end(context_table [session_id], str(bot_input.get('logs')))
        #Delete the context
        del context_table [session_id]

    else:
    # At beginning of conversation, create the context for new conversation
        if intent.startswith("Welcome"):
            #Create a new context
            context_table [session_id] = {"user_name": "", "mode": "faq_mode"}
            print ("Context Table ",context_table) # For debugging

        # Update the current context
        current_context = context_table [session_id]
        current_context["intent"] = intent

        # Process the intent. If in survey mode, get the next question
        if current_context["mode"] == "survey_mode":
            bot_resp = get_next_question (current_context, bot_input)
        else:
            bot_resp = process_response (current_context, bot_input)

        print(bot_resp) # For debugging

    # Return the response for POST request from chatbot webhook
    return bot_resp

@app.post('/beso/RHBv3/reload')
async def reload_dataframes(request: Request):
    # Clear existing dataframes
    intent_table = pd.DataFrame()
    context_table = {}

    # Load intent table and open response database
    intent_table = load_intent_table()
    open_response_db()

    # Reload the webhook_main module using importlib.reload()
    reload(webhook_main)

    # Return a success message
    return 'Dataframes reloaded successfully.'