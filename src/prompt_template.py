#install Langchain with PIP

from langchain.prompts import PromptTemplate

# Define a template for generating prompts
template = "You are a helpful assistant. Please answer the following question: {question}"

# Create a PromptTemplate object
prompt_template = PromptTemplate(template=template, input_variables=["question"])

# Generate a prompt using the template
question = "What is the capital of France?"
prompt = prompt_template.render(question=question)

print(prompt)
