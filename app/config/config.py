# constants.py
import os
import assemblyai as aai
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
outline_prompt_template_path = os.path.join(base_dir, "prompt_template", "outline_prompt.txt")
data_rich_template_path = os.path.join(base_dir, "prompt_template", "data_rich_prompt.txt")
transcript_path = os.path.join(base_dir, "input", "transcript.txt")
output_filename = "output.md"

# Model configurations
outline_model_engine = os.environ.get("OUTLINE_MODEL")
datarich_model_engine = os.environ.get("DATARICH_MODEL")
claude_api_key = os.environ.get("CLAUDE_API_KEY")
max_token = os.environ.get('MAX_TOKEN')
temperature = os.environ.get('TEMPERATURE')

aai.settings.api_key = os.environ['AAI_API_KEY']

# Prompt variables
prompt_variable = {
    "transcript": "transcript",
    "output": "result",
}