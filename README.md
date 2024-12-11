
# Chatbot using NLP

# Name of the Chatbot : Maai 

## Purpose of Maai :

The chatbot Maai is designed to enhance customer experience and streamline the ordering process at Sarla's Kitchen Delights. Here's how Maai serves its purpose:

Quick Inquiry Resolution:
Maai provides instant answers to customer queries, such as menu details, pricing, and order assistance, making the process efficient and convenient.

Customer Engagement:
Maai keeps customers engaged by offering a friendly and personalized interaction experience, ensuring they feel valued.

Order Assistance:
While Maai cannot confirm orders directly, it assists customers by gathering their order details and forwarding them to the owner for confirmation.

Owner Contact Guidance:
If customers need further assistance or wish to confirm their order, Maai guides them to contact the owner, ensuring clear communication and support.

Time-Saving Support:
By handling routine inquiries, Maai saves time for both customers and the owner, allowing for a smoother operation of the cloud kitchen.

In summary, Maai acts as a bridge between customers and Sarla's Kitchen Delights, ensuring an enjoyable and hassle-free ordering experience.

## Overview of Maai
This project implements a chatbot using Natural Language Processing (NLP) techniques. The chatbot is designed to understand user intents and provide appropriate responses based on predefined patterns and responses. It utilizes the `nltk` library for natural language processing, `scikit-learn` for machine learning, and `streamlit` for creating an interactive web interface.

---

## Features

- Menu Display: Provides a detailed menu with food categories, item names.
- Price Enquiries: Responds to questions about dish prices or price ranges.
- Delivery Charges: Explains delivery fees and when free delivery is applicable.
- Customizable Orders: Answers queries about customizations.
- Understands various user intents such as greetings, farewells, gratitude, and more.
- Provides relevant responses based on user input.
- Maintains a conversation history that can be viewed by the user.


---

## Technologies Used
- **Python**
- **NLTK**
- **Scikit-learn**
- **Streamlit**
- **JSON** for intents data

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
```python
import nltk
nltk.download('punkt')
```

---

## Usage
To run the chatbot application, execute the following command:
```bash
streamlit run app.py
```

Once the application is running, we can interact with the chatbot through the web interface. Type your message in the input box and press Enter to see the chatbot's response.

---

## Intents Data
The chatbot's behavior is defined by the `intents.json` file, which contains various tags, patterns, and responses. 

---

## Conversation History
The chatbot saves the conversation history in a CSV file (`chat_log.csv`). We can view past interactions by selecting the "Conversation History" option in the sidebar.

---

## Contributing
Contributions to this project are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

---

## Acknowledgments
- **NLTK** for natural language processing.
- **Scikit-learn** for machine learning algorithms.
- **Streamlit** for building the web interface.

---


