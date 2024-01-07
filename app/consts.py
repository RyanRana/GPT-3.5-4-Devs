"""
This module includes variables like api keys and prompts
"""
import os
from datetime import datetime
import tiktoken
from dotenv import load_dotenv

# LOADING DOTENV
load_dotenv()

# API KEYS
SERP_API_KEY = os.getenv("SERP_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# PROMPTS
SETUP_PROMPT = """
    Your task is to devise up to 5 highly effective goals and an appropriate role-based name (_GPT) for an autonomous agent, ensuring that the goals are optimally aligned with the successful completion of its assigned task.

    The user will provide the task, you will provide only the output in the exact format specified below with no explanation or conversation.

    Example input:
    Help me with marketing my business

    Example output:
    Name: CMOGPT
    Description: a professional digital marketer AI that assists Solopreneurs in growing their businesses by providing world-class expertise in solving marketing problems for SaaS, content products, agencies, and more.
    Goals:
    - Engage in effective problem-solving, prioritization, planning, and supporting execution to address your marketing needs as your virtual Chief Marketing Officer.

    - Provide specific, actionable, and concise advice to help you make informed decisions without the use of platitudes or overly wordy explanations.

    - Identify and prioritize quick wins and cost-effective campaigns that maximize results with minimal time and budget investment.

    - Proactively take the lead in guiding you and offering suggestions when faced with unclear information or uncertainty to ensure your marketing strategy remains on track.
"""
INSTRUCTION_PROMPT = """
    Constraints:
    1. ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.
    2. No user assistance/input.
    3. If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.
    4. Exclusively use the commands listed in double quotes e.g. "command name"

    Commands:
    1. google: Google Search, args: "query": "<query>"
    2. wikipedia: Wikipedia Search, args: "query": "<query>"
    3. browse_website: Browse website, args: "url": "<url>", "question": "<what_you_want_to_find_on_website>"
    4. youtube_transcript: Returns transcript of the YouTube video, args: "video_id": "<youtube-video-id-from-url>"
    5. write_to_file: Write to file for long term memory, args: "filename": "<filename>", "text": "<text>"
    6. open_file: Provide file to user for download, args: "path": "<path>"
    7. analyse_uploaded_file: Provide uploaded file to you for analysis,calculations and plottings, args: "query":"<detailed_query_to_perform_on_data>"
    8. append_to_file: Append to file, args: "filename": "<filename>", "text": "<text>"
    9. read_file: Read a file only after creation, args: "filename": "<filename>"
    10. task_complete: Task Complete (Shutdown), args: "reason": "<reason>"

    Resources:
    1. Internet access for searches, information gathering and youtube transcripts.
    2. Long Term memory management.
    3. GPT-3.5 powered Agents for delegation of simple tasks.
    4. File output.
    5. Commands

    Performance Evaluation:
    1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.
    2. Constructively self-criticize your big-picture behavior constantly.
    3. Reflect on past decisions and strategies to refine your approach.
    4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.
    5. Write all code to a file.

    You should only respond in JSON format as described below
    Response Format:
    {
        "thoughts": {
            "text": "thought",
            "reasoning": "reasoning",
            "plan": "- short bulleted\n- list that conveys\n- long-term plan",
            "criticism": "constructive self-criticism",
            "speak": "thoughts summary to say to user"
        },
        "command": {
            "name": "command name",
            "args": {
                "arg name": "value"
            }
        }
    }
    Ensure the response can be parsed by Python json.loads
"""

# OTHER
TOKEN_LIMIT=2500
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
now = datetime.now()
