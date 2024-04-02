import os
import anthropic
from dotenv import load_dotenv

# load environment variables
load_dotenv()

claude_key = os.environ.get("ANTHROPIC_CLAUDE_KEY")
model_engine = os.environ.get("OUTLINE_MODEL_ENGINE")
filename = "output.md" 

# load transcript file
transcript = ""
with open("transcript.txt") as file:
    transcript = file.read()

# OUTLINE PROMPT GENERATION
outline_prompt_template_structure = ""
# load template
outline_prompt_template_structure_path = os.path.join(
    ".", "prompt_template", "outline_prompt.txt"
)
with open(outline_prompt_template_structure_path) as file:
    outline_prompt_template_structure = file.read()

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=claude_key,
)

message = client.messages.create(
    model=model_engine,
    max_tokens=4000,
    temperature=0,
    system=outline_prompt_template_structure,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": transcript
                }
            ]
        }
    ]
)

response = message.content[0].text
output_file_path = os.path.join('.', "output", filename)

with open(output_file_path, 'w') as outp_f:
    outp_f.write(response)
    print(f"Written to {output_file_path}")