import os

claude_key = os.environ.get("ANTHROPIC_CLAUDE_KEY")
outline_model_engine = os.environ.get("OUTLINE_MODEL_ENGINE")
datarich_model_engine = os.environ.get("DATARICH_MODEL_ENGINE")
max_token = os.environ.get("MAX_TOKEN") 
temprature = os.environ.get("TEMPRATURE")

filename = "output.md"

# prompt vars
prompt_variable = {
    "transcript": "transcript",
    "outline": "outline",
    "output": "elaboration"
}

transcript_path = os.path.join(".", "transcript.txt")
outline_prompt_template_path = os.path.join(".", "prompt_template", "outline_prompt.txt")
data_rich_template_path = os.path.join(".", "prompt_template", "data-rich_prompt.txt")
