import os
import signal

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface


load_dotenv()

agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")

if not agent_id or not api_key:
    raise ValueError("Missing AGENT_ID or ELEVENLABS_API_KEY in .env")

elevenlabs = ElevenLabs(api_key=api_key)

conversation = Conversation(
    elevenlabs,
    agent_id,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=lambda response: print(f"Vox: {response}"),
    callback_user_transcript=lambda transcript: print(f"You: {transcript}"),
)

conversation.start_session()

signal.signal(
    signal.SIGINT,
    lambda sig, frame: conversation.end_session()
)

conversation_id = conversation.wait_for_session_end()

print(f"Conversation ID: {conversation_id}")