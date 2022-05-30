from google.cloud import dialogflow
import os
from src.model.message import Answer

class DialogflowController():
    async def detect_intent(project_id, session_id, text, language_code):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        
        response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )
        
        answer = Answer
        return format(response.query_result.fulfillment_text)
        # return answer
