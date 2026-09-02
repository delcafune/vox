# Vox 🎙️

Vox is a voice assistant I built in Python using ElevenLabs Conversational AI.

You can speak to Vox through your microphone and have a natural voice conversation with it. I also added a few simple tools that let Vox interact with my Mac, such as opening websites, opening selected apps, and telling the current time.

## Features

- Talk to Vox using your microphone
- Have natural AI voice conversations
- Open websites with voice commands
- Open Calculator, Notes, or Spotify
- Ask for the current time and date
- End the conversation by saying goodbye

## Technologies Used

- Python
- ElevenLabs Conversational AI
- ElevenLabs Python SDK
- PyAudio
- python-dotenv

## How to Run

1. Clone this repository.

2. Create and activate a Python virtual environment.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create an ElevenLabs account and set up a Conversational AI agent.

5. Create a `.env` file in the project folder and add:

```env
ELEVENLABS_API_KEY=your_api_key
AGENT_ID=your_agent_id
```

6. Run Vox:

```bash
python main.py
```

You can then start speaking to Vox through your microphone.

> An ElevenLabs API key and Agent ID are required to run the voice assistant. These are not included in the repository for security reasons.

## What I Learned

Building Vox helped me learn how to connect Python to an external AI service, work with environment variables and API keys, handle microphone/audio input, create tools that an AI agent can call, and use Git and GitHub to manage a project.