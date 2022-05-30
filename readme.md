# chatbotAPI
An API running on Heroku servers, responsible for allowing communication between a user and a chatbot created using dialogflow.

# Routes
###### baseURL
https://bsf-chatbot.herokuapp.com/

###### POST
/send-message - requires as a parameter a JSON containing text, email and sessionID and returns another JSON with botResponse. sessionID must remain consistent between each call to stay in the same conversation.