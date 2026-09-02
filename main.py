import os
import signal
import webbrowser
import subprocess

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation, ClientTools
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface


def open_website(parameters):
    url = parameters.get("url")

    if not url:
        return

    if not url.startswith(("https://", "https://")):
        if "." not in url:
            url = url + ".com"

        url = "https://" + url

    webbrowser.open(url)

def open_app(parameters):
    app_name = parameters.get("app")

    allowed_apps = {
        "calculator": "Calculator",
        "notes": "Notes",
        "spotify": "Spotify",
    }

    if app_name not in allowed_apps:
        print("App not allowed.")
        return

    subprocess.run(["open", "-a", allowed_apps[app_name]])

TEST_MODE = True

load_dotenv()

agent_id = os.getenv("AGENT_ID")
api_key = os.getenv("ELEVENLABS_API_KEY")

if not agent_id or not api_key:
    raise ValueError("Missing AGENT_ID or ELEVENLABS_API_KEY in .env")

elevenlabs = ElevenLabs(api_key=api_key)

client_tools = ClientTools()
client_tools.register("openWebsite", open_website)

conversation = Conversation(
    elevenlabs,
    agent_id,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    client_tools=client_tools,
    callback_agent_response=lambda response: print(f"Vox: {response}"),
    callback_user_transcript=lambda transcript: print(f"You: {transcript}"),
)

if TEST_MODE:
    print("Vox is running in TEST MODE")

    app = input("App to open: ").lower()

    open_app({"app": app})

    raise SystemExit

conversation.start_session()

def stop_vox(sig, frame):
    print("\nStopping Vox...")
    conversation.end_session()

signal.signal(signal.SIGINT, stop_vox)

conversation_id = conversation.wait_for_session_end()

print(f"Conversation ID: {conversation_id}")