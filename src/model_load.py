from transformers import AutoTokenizer, AutoModelForCausalLM,pipeline,GenerationConfig
from langchain.llms import HuggingFacePipeline
from dotenv import load_dotenv
import os

# loading .env
load_dotenv()

MODEL_NAME = os.getenv('MODEL_NAME')
MODEL_FILE = os.getenv('MODEL_FILE')

def load_model_LC():

    # Loading the tokenzier
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME,use_fast=True)

    # Loading the LLM model from HF or .cache directory
    base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME,
                                                    revision=MODEL_FILE,
                                                    device_map='auto'
                                                    )

    # Creating general configuration
    generation_config = GenerationConfig.from_pretrained(MODEL_NAME)
    generation_config.max_new_tokens = 512
    generation_config.temperature = 0.47
    generation_config.remove_invalid_values = True
    generation_config.do_sample = True

    # Creating the pipeline
    model_pipe = pipeline(task='text-generation',
                        model=base_model,
                        tokenizer=tokenizer,
                        generation_config=generation_config
                        )

    # Intergarting the Model into Langchain
    LC_model = HuggingFacePipeline(pipeline=model_pipe,
                                    model_kwargs={'temperature':0.47,
                                                'max_new_tokens':512,
                                                }
                                )

    return LC_model
