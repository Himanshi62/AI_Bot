# AI-Driven Conversational Bot for Customer Support

This project is an AI-driven conversational bot designed to handle customer support queries using Generative AI models like OpenAI's GPT-3. The bot supports multiple messaging channels such as SMS, WhatsApp, and RCS, and integrates with APIs like Twilio to handle communication.


## Project Overview
The AI-driven conversational bot handles customer support queries, generating contextually appropriate responses using OpenAI's Generative AI models. It can receive and respond to messages across multiple channels like SMS and WhatsApp using Twilio APIs. The bot also includes a feedback mechanism for continuous improvement.

## Features
- **Multi-Channel Support**: Communicates via SMS, WhatsApp, and RCS.
- **Generative AI Integration**: Uses GPT-3 for generating responses.
- **In-Memory Data Storage**: Stores conversation history and feedback.
- **Fallback Mechanism**: Static responses in case of AI service unavailability.
- **Robust API**: RESTful endpoints for query handling and feedback.

## Tech Stack
- **Backend Framework**: Django, Django REST Framework
- **Generative AI API**: OpenAI's GPT-3
- **Messaging Service**: Twilio API for SMS and WhatsApp
- **Database**: SQLite (for lightweight data storage)
- **Testing**: Unit tests and integration tests

## Installation and Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yadavbalbir/ai-support-bot.git
   cd ai-support-bot

1. **Create a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Migrate the database**:

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser** (to access the Django admin panel):

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

## Configuration

### Twilio Configuration

1. Sign up for a Twilio account and get your **Account SID**, **Auth Token**, and phone numbers.
2. Set up a WhatsApp sandbox in Twilio.
3. Update your `settings.py` file with the following:

    ```python
    TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
    TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
    TWILIO_WHATSAPP_NUMBER = 'your_twilio_whatsapp_sandbox_number'
    ```

