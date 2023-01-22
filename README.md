<hx>openai_home_assistant</hx>
This project uses the OpenAI API to generate text based on the status of a home appliance, such as a washing machine or a dryer. The generated text is then sent to a Telegram chat using the MQTT protocol.

<b>Getting Started</b>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<b>Prerequisites</b>
To run this project, you will need:

A running MQTT broker
An OpenAI API key
A Telegram bot and chat ID
Python 3 installed on your machine
The following Python libraries:
- paho-mqtt
- openai

You can install these libraries using pip:
<i>pip install paho-mqtt openai</i>

<b>Installing</b>
1. Clone this repository to your local machine
<i>git clone https://github.com/phoenix-blue/openai_home_assistant.git</i>

2. Replace the placeholders in the run.py script with your own MQTT broker details, OpenAI API key and Telegram chat ID.

3. Replace the placeholders in the dryer.yaml and Telegram_Output.yaml files with your own MQTT broker details and Telegram chat ID.

4. Run the run.py script

<b>Usage</B>
When the status of the home appliance changes, the dryer.yaml script will send a message to the openai/status topic on the MQTT broker. The run.py script will listen for messages on this topic and use the OpenAI API to generate a response based on the received status. The generated text will then be sent to the Telegram chat through the Telegram_Output.yaml script.

<b>note</b>
Complete project is build with the openai environment, next step is to generate an way to run the python script direct in HASSIO OS.


