import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
        
counter = 0

def main():
    global counter
    st.title("Welcome to Maai - A chatbot for Sarla's Kitchen Delights!")

    # Create a sidebar menu with options
    menu = ["Maai-Chatbot", "Home", "Conversation History", "About Maai", "Contact Us"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home Menu
    if choice == "Maai-Chatbot":
        st.write("Welcome Dear Customer, Talk to our chatbot for assistance or any query.")

        # Check if the chat_log.csv file exists, and if not, create it with column names
        if not os.path.exists('chat_log.csv'):
            with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])

        counter += 1
        user_input = st.text_input("You:", key=f"user_input_{counter}")

        if user_input:

            # Convert the user input to a string
            user_input_str = str(user_input)

            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=500, max_chars=None, key=f"chatbot_response_{counter}")

            # Get the current timestamp
            timestamp = datetime.datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

            # Save the user input and chatbot response to the chat_log.csv file
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([user_input_str, response, timestamp])

            if response.lower() in ['goodbye', 'bye']:
                st.write("Dear Customer,Thank you so much for visiting Maai!")
                st.stop()

    elif choice == "Home":
        #Display the information about Sarla's Kitchen Delight
        st.write("Welcome to Sarla's Kitchen Delights, your go-to destination for authentic homemade food! Our mission is to bring the comfort and warmth of homemade meals straight to your table, ensuring you enjoy every bite of delicious, freshly prepared dishes.")
        st.write("At Sarla's Kitchen Delights, we understand the value of time and the joy of home-cooked food. That’s why we’ve made it easy for you to order your favorite meals online, even in advance, so you can plan your day without missing out on the goodness of homemade flavors.")
        st.write("To make your experience seamless, we’ve introduced Maai, our friendly customer service chatbot. Whether you want to place an order, explore our menu, check prices, or get assistance with any queries, Maai is here to help 24/7. If you still have unanswered questions, you can always reach out to the owner for further support.")
        st.write("Sarla's Kitchen Delights is more than just a food service—it's a bridge to your home, one meal at a time. We’re here to ensure you enjoy healthy, tasty, and satisfying meals without the hassle of cooking.")
        st.write("Thank you for choosing Sarla's Kitchen Delights. Let us serve you the comfort of homemade food with just a click!")
    # Conversation History Menu
    elif choice == "Conversation History":
        # Display the conversation history in a collapsible expander
        st.header("Conversation History")
        # with st.beta_expander("Click to see Conversation History"):
        with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                st.text(f"User: {row[0]}")
                st.text(f"Chatbot: {row[1]}")
                st.text(f"Timestamp: {row[2]}")
                st.markdown("---")

    elif choice == "About Maai":
        st.write(" Meet Maai, your personal food assistant at Sarla's Kitchen Delights! Maai is our smart and friendly customer service chatbot, designed to make your experience smooth and hassle-free. Whether you’re looking to explore our menu, check prices, place an order for delicious homemade food, or plan your meals in advance, Maai is here to assist you every step of the way. The chatbot is built using Natural Language Processing (NLP) library and Logistic Regression, to extract the intents and entities from user input. The chatbot is built using Streamlit, a Python library for building interactive web applications.")

        st.subheader("Project Overview:")

        st.write("""
        The project is divided into two parts:
        1. NLP techniques and Logistic Regression algorithm is used to train the chatbot on labeled intents and entities.
        2. For building the Chatbot interface, Streamlit web framework is used to build a web-based chatbot interface. The interface allows users to input text and receive responses from the chatbot.
        """)

        st.subheader("Dataset:")

        st.write("""
        The dataset used in this project is a collection of labelled intents and entities. The data is stored in a list.
        - Intents: The intent of the user input (e.g. "greeting", "Menu", "Order food")
        - Entities: The entities extracted from user input (e.g. "Hi", "What are the food items?", "What is cost of Masala Dosa?")
        - Text: The user input text.
        """)

        st.subheader("Streamlit Chatbot Interface:")

        st.write("The chatbot interface is built using Streamlit. The interface includes a text input box for users to input their text and a chat window to display the chatbot's responses. The interface uses the trained model to generate responses to user input.")

        st.subheader("Conclusion:")

        st.write("In this project, a chatbot is built that can understand and respond to user input based on intents. The chatbot was trained using NLP and Logistic Regression, and the interface was built using Streamlit. This project can be extended by adding more data, using more sophisticated NLP techniques, deep learning algorithms.")

    elif choice == "Contact Us":
        st.subheader(" Name of the Owner - Sarla")
        st.write("Sarla's Mobile Number : 123456789 ")
        st.write("Sarla's Delight Kitchen Address : Gwalior, Madhya Pradesh")

if __name__ == '__main__':
    main()
