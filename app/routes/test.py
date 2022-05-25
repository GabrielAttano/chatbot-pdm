from google.cloud import dialogflow
import os

# credential_path = 'C:\\Users\\t6w31\\Desktop\\dialogflow\\testagent-wfsa-62699a01dcc3.json'
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

async def detect_intent(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    session = session_client.session_path(project_id, session_id)
    
    query_input = dialogflow.QueryInput(text=text_input)
    
    response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
    
    return format(response.query_result.fulfillment_text)