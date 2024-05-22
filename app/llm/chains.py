from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain

from . import utils
from . import config

def load_prompts(prompt_template_path: str) -> PromptTemplate:
    """Load prompt templates from files."""
    return PromptTemplate.from_file(prompt_template_path)


def load_llms(model: str, prompt: PromptTemplate) -> ChatAnthropic:
    """Load language models and create LLM chains."""
    llm = ChatAnthropic(
        anthropic_api_key=config.claude_api_key,
        model_name=model,
        max_tokens=config.max_token,
        temperature=config.temperature,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def summarize_transcript(transcript: str) -> str:
    outline_prompt = load_prompts(config.outline_prompt_template_path)
    data_rich_prompt = load_prompts(config.data_rich_template_path)
    
    outline = load_llms(
        model=config.outline_model_engine, 
        prompt=outline_prompt
    )
    data_rich = load_llms(
        model=config.datarich_model_engine, 
        prompt=data_rich_prompt
    )
    
    ss_chain = SimpleSequentialChain(
        chains=[outline, data_rich],
        input_key=config.prompt_variable["transcript"],
        output_key=config.prompt_variable["output"],
        verbose=False,
    )

    result = ss_chain.run(transcript=transcript)
    return result


if __name__ == "__main__":
    transcript = utils.load_file(config.transcript_path)
    summarize_transcript(transcript)