# views.py
from django.shortcuts import render
from .forms import UserInputForm
from .models import ChatMessage
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.template import loader

chatbot = ChatBot('HashConGTP')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)

def trainBot(chatbot):
    pass

def handler(request):
    template = loader.get_template('homePage.html')
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            # Save user message to the database
            ChatMessage.objects.create(user='User', content=user_message)
            # Get chatbot response
            chatbot_response = chatbot.get_response(user_message)
            # Save chatbot response to the database
            ChatMessage.objects.create(user='Chatbot', content=str(chatbot_response))
    else:
        form = UserInputForm()

    # Fetch all chat messages from the database
    chat_messages = ChatMessage.objects.all()

    return render(request, 'homePage.html', {'form': form, 'chat_messages': chat_messages})