#!/usr/bin/env python
import os

# from rasa.core.agent import Agent
# from rasa_addons.webchat import WebChatInput, SocketInputChannel
# load your trained agent
from rasa.core.agent import Agent
from rasa.core.channels import SocketIOInput

agent = Agent.load('models/20191223-210944.tar.gz')

input_channel = SocketIOInput(
    # event name for messages sent from the user
    user_message_evt="user_uttered",
    # event name for messages sent from the bot
    bot_message_evt="bot_uttered",
    # socket.io namespace to use for the messages
    namespace=None
)

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5500)