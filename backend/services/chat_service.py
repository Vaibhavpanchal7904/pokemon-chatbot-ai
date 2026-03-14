from backend.chatbot.agent import agent


class ChatService:

    # normal response (optional)
    def chat(self, message):

        response = agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": message}
                ]
            },
            config={"configurable": {"thread_id": "pokemon-chat"}}
        )

        return response["messages"][-1].content


    # streaming response (for real AI typing)
    def stream_chat(self, message):

        stream = agent.stream(
            {
                "messages": [
                    {"role": "user", "content": message}
                ]
            },
            config={"configurable": {"thread_id": "pokemon-chat"}}
        )

        for chunk in stream:

            if "messages" in chunk:

                msg = chunk["messages"][-1]

                if msg.content:
                    yield msg.contentll