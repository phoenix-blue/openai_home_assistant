import paho.mqtt.client as mqtt
import openai

# MQTT broker details
broker_address = "IP_BROKER"
username = "USER"
password = "PASS"

# OpenAI API key
openai_api_key = "API"
openai.api_key = openai_api_key

# MQTT client
client = mqtt.Client()
client.username_pw_set(username, password)
client.connect(broker_address)

# Subscribe to openai/status topic
client.subscribe("openai/status")

# Callback function for received messages
def on_message(client, userdata, message):
    status = str(message.payload)
    print("Received message: " + status)


    # Build the prompt using the received status
    prompt = "Create a random text with the following status:" + status + ". "

    # Generate response using OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=40,
        temperature=0.9
    )

    # Publish response to openai/output topic
    client.publish("openai/output", response["choices"][0]["text"])

# Assign callback function
client.on_message = on_message

# Start MQTT loop
client.loop_forever()
