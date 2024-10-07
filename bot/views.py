import openai
from AISupportBot import settings
from Utils.chatCompletion import SupportWithChatCompletion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client
from bot.models import Conversation
from bot.serializers import ConversationSerializer

class HiMessage(APIView):
    def get(self, request):
        return Response({"message": "Hi"}, status=status.HTTP_200_OK)
    
class CustomerSupportView(APIView):
    def get(self, request):
        query = request.query_params.get('query', 'there')
        response_message = SupportWithChatCompletion(query)
        return Response({"message": response_message}, status=status.HTTP_200_OK)


class QueryView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        message = request.data.get('message')

        if not user_id or not message:
            return Response({"error": "user_id and message are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Call GPT-3 API
        response_text = SupportWithChatCompletion(message)

        # Save the conversation to DB
        conversation = Conversation.objects.create(user_id=user_id, message=message, response=response_text)
        serializer = ConversationSerializer(conversation)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SendMessageView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        message = request.data.get('message')
        channel = request.data.get('channel')  

        if not user_id or not message or not channel:
            return Response({"error": "user_id, message, and channel are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Send message using Twilio
        try:
            response_sid = self.send_message_via_twilio(user_id, message, channel)
            return Response({"status": "Message sent", "sid": response_sid}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def send_message_via_twilio(self, to, body, channel):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

        if channel == "sms":
            from_ = settings.TWILIO_PHONE_NUMBER
        elif channel == "whatsapp":
            from_ = 'whatsapp:' + settings.TWILIO_WHATSAPP_NUMBER
        else:
            raise ValueError("Unsupported channel")

        message = client.messages.create(
            body=body,
            from_=from_,
            to=to
        )
        return message.sid

    