import warnings
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
import utils
import constants
from constants import outline_prompt_template_path, data_rich_template_path, \
    outline_model_engine, datarich_model_engine, claude_key, max_token, \
    temprature, prompt_variable

#/ Load environment variables
load_dotenv(find_dotenv())

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    
# Load transcript file
transcript: str = utils.load_file(constants.transcript_path)

# struct prompt
outline_prompt: PromptTemplate = PromptTemplate.from_file(
    template_file=outline_prompt_template_path
)

data_rich_prompt: PromptTemplate = PromptTemplate.from_file(
    template_file=data_rich_template_path
)

# llm
outline_llm = ChatAnthropic(
    anthropic_api_key=claude_key,
    model_name=outline_model_engine,
    max_tokens=max_token,
    temperature=temprature
)
data_rich_llm = ChatAnthropic(
    anthropic_api_key=claude_key,
    model_name=datarich_model_engine,
    max_tokens=max_token,
    temperature=temprature
)

# struct chains
outline_chains = LLMChain(llm=outline_llm, prompt=outline_prompt)
data_rich_chains = LLMChain(llm=data_rich_llm, prompt=data_rich_prompt)

print(prompt_variable)

ss_chain = SimpleSequentialChain(
    chains=[outline_chains, data_rich_chains],
    input_key=prompt_variable["transcript"],
    output_key=prompt_variable["output"],
    verbose=True
)

result = ss_chain.run(transcript=transcript)

utils.save_file(result, constants.filename)