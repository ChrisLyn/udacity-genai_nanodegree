#A starter file for the HomeMatch application if you want to build your solution in a Python program instead of a notebook. 

import os
import pandas as pd
os.environ["OPENAI_API_KEY"] = "YOU_API_KEY"
os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"

from langchain.llms import OpenAI

