import streamlit as st

# Page settings
st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖"
)

# Chatbot responses
responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Hey! How can I help you?",

    "how are you": "I am doing well. How about you?",
    "what is your name": "My name is RuleBot.",
    "who created you": "I was created using Python.",
    "where are you from": "I live inside your computer!",
    "how old are you": "I don't have an age like humans.",

    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that allows systems to learn from data.",
    "what is python": "Python is a popular programming language.",
    "what is coding": "Coding is the process of writing instructions for computers.",

    "tell me a joke": "Why do programmers hate nature? It has too many bugs!",
    "tell me another joke": "Why did the computer go to the doctor? Because it caught a virus!",

    "what is your favorite color": "I like all colors equally!",
    "what is your favorite food": "I don't eat food, but I process data.",
    "can you sing": "Sorry, I can only chat for now.",
    "can you dance": "Not yet, maybe in the next update!",

    "good morning": "Good Morning! Have a wonderful day.",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "good night": "Good Night! Sleep well.",

    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "sorry": "No problem!",

    "what day is today": "I can't check the date right now.",
    "what time is it": "I can't check the time right now.",

    "who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
    "what is the capital of india": "New Delhi is the capital of India.",
    "what is the largest planet": "Jupiter is the largest planet in our Solar System.",
    "who is the father of india": "Mahatma Gandhi is known as the Father of the Nation.",

    "what is your purpose": "My purpose is to help and answer simple questions.",
    "are you human": "No, I am a chatbot.",
    "do you like humans": "Yes! Humans are amazing creators.",

    "bye": "Goodbye! Have a great day!"
}

# Title
st.title("🤖 Rule-Based AI Chatbot")
st.write("Ask me a question!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Bot response
    clean_input = user_input.lower().strip()

    if clean_input in ["exit", "quit", "close"]:
        bot_reply = "👋 Goodbye! Thanks for chatting with me."
    else:
        bot_reply = responses.get(
            clean_input,
            "Sorry, I don't understand that. Try another question."
        )

    # Show bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)


