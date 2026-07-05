from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from django.conf import settings
from .knowledge import SYSTEM_PROMPT

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4,
    api_key=settings.GROQ_API_KEY,
)

class ChatbotAskView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user_message = request.data.get('message', '').strip()
        history = request.data.get('history', [])

        if not user_message:
            return Response({'error': 'No message provided'}, status=400)

        messages = [SystemMessage(content=SYSTEM_PROMPT)]

        for turn in history[-8:]:
            if turn.get('sender') == 'user':
                messages.append(HumanMessage(content=turn.get('text', '')))
            else:
                messages.append(AIMessage(content=turn.get('text', '')))

        messages.append(HumanMessage(content=user_message))

        try:
            result = llm.invoke(messages)
            reply_text = result.content
        except Exception as e:
            print("=== CHATBOT ERROR ===")
            print(e)
            print("======================")
            reply_text = "Sorry, I'm having trouble connecting right now. Please contact us at +91 8200455307."

        return Response({'reply': reply_text})