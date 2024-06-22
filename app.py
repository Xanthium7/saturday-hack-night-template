
import os
from langchain_openai import ChatOpenAI
# from langchain.chat_models import ChatOpenAI
from openai import OpenAI as OAI
# from s import openaikey
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from dotenv import load_dotenv

load_dotenv()

openaikey = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_API_KEY'] = openaikey


client = OAI(api_key=openaikey)


audio_file = open("a.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)
# print(transcription)
transcription = "create me a single page cool resturant website with navbar each food listing"


# llm = OpenAI(model_name="gpt-4o", temperature=0.6)
llm = ChatOpenAI(model_name='gpt-4')


p_template_name = PromptTemplate(
    input_variables=['transcription'],
    template="You are a prompt generating bot that will take an instruction about a website and u will need to describe that website clealrly. You should describe the need of any stylings, animations or images that may be required.It should have a default font of Arial, unless specified differently. (You will be giving these instructions to a coding bot that will genrate the html css and js code). Keep the instructions less than 150 words. your given the instruction :{transcription}."

)
p_template_name.format(
    transcription=transcription)

prompt_chain = LLMChain(llm=llm, prompt=p_template_name,
                        output_key="prompt")

prompt_return = prompt_chain(transcription)
prompt = prompt_return['prompt']

print("\n\n\n", prompt)


def generate_html_sections(prompt):
    sections = ['navbar', 'main-content', 'footer']
    complete_html = """<!DOCTYPE html>\n<link rel="stylesheet" href="output.css">\n<script src="output.js"></script>\n<html>\n"""
    for section in sections:
        # Concise prompt for each section
        section_prompt = f"Generate the {section} of an HTML page based on: {prompt}. Make sure to give the code ONLY for the {section} and nothing more. Include necessary classes and ids for each element. Exclude the css code and javascript code. Give back the html code as plain text (make sure the response does not contain '```' tag). (if at any point,any images are needed to be added then use 'https://placehold.co/600x400' as the image source)"
        p_template_html_section = PromptTemplate(
            input_variables=['transcription'],
            template=section_prompt
        )
        code_html_chain_section = LLMChain(
            llm=llm, prompt=p_template_html_section, output_key="html_code_section")
        result_section = code_html_chain_section(
            {"transcription": transcription})
        html_section = result_section["html_code_section"]
        # Add the generated section to the complete HTML
        if section == 'header':
            complete_html += "<head>\n" + html_section + "\n</head>\n<body>\n"
        elif section == 'footer':
            complete_html += html_section + "\n</body>\n</html>"
        else:
            complete_html += html_section + "\n"
    return complete_html


def sanitize_for_format(string):
    # Replace single curly braces with doubled curly braces to escape them
    return string.replace("{", "").replace("}", "")


def generate_css_sections(prompt, html_code):
    sections = ['navbar', 'main-content', 'footing']
    complete_css = ""
    for section in sections:
        # Sanitize prompt and html_code to escape curly braces
        sanitized_prompt = sanitize_for_format(prompt)
        sanitized_html_code = sanitize_for_format(html_code)

        section_prompt = f"Create the {section} CSS code stylings based on the website description: {sanitized_prompt} and the HTML code: {sanitized_html_code}. Give only the css code as plain text (make sure the response does not contain '```' tag). use proper classes or ids as used in the html code"

        # Debugging: Print the section prompt to ensure it's formatted correctly
        # print(f"Section Prompt: {section_prompt}")

        p_template_css_section = PromptTemplate(
            input_variables=['prompt', 'html_code'],
            template=section_prompt
        )

        # Prepare the input dictionary with original (unsanitized) values
        input_dict = {"prompt": prompt, "html_code": html_code}

        # Debugging: Print the input dictionary to ensure it's correct
        # print(f"Input Dictionary: {input_dict}")

        code_css_chain_section = LLMChain(
            llm=llm, prompt=p_template_css_section, output_key="css_code_section"
        )

        result_section = code_css_chain_section(input_dict)
        css_section = result_section["css_code_section"]
        complete_css += css_section + "\n"

    return complete_css


def generate_js_sections(prompt, html_code):
    sections = ['dynamic-content-loadings']
    complete_js = ""
    for section in sections:
        sanitized_prompt = sanitize_for_format(prompt)
        sanitized_html_code = sanitize_for_format(html_code)
        # Modify the prompt to request a specific section of the JavaScript
        section_prompt = f"Create the {section} using JavaScript code based on the website description: {sanitized_prompt}, the HTML code: {sanitized_html_code} Give only the javascript code as plain text (make sure the response does not contain '```' tag) and nothing else"
        p_template_js_section = PromptTemplate(
            input_variables=['prompt', 'html_code'],
            template=section_prompt
        )
        code_js_chain_section = LLMChain(
            llm=llm, prompt=p_template_js_section, output_key="js_code_section")
        result_section = code_js_chain_section(
            {"prompt": prompt, "html_code": html_code})
        js_section = result_section["js_code_section"]
        complete_js += js_section + "\n"
    return complete_js


html_code = generate_html_sections(prompt)

# print("\n\n\n", html_code)
css_code = generate_css_sections(prompt, html_code)

# print("\n\n\n", css_code)
js_code = generate_js_sections(prompt, html_code)

# print("\n\n\n", js_code)

# Save the generated code to files
with open('output.html', 'w') as f:
    f.write(html_code)
with open('output.css', 'w') as f:
    f.write(css_code)
with open('output.js', 'w') as f:
    f.write(js_code)

# p_template_html = PromptTemplate(
#     input_variables=['prompt'],
#     template="create me an html skeleton code for the following website: {prompt}. Make sure there is 'style' tags in the html file and  'scripts' tag in the html file. Only return the html code and nothing else. the html header should contain link rel stylesheet to output.css file in the same directory as well as it should also link output.js file in the same directory to the html file"

# )

# code_html_chain = LLMChain(llm=llm, prompt=p_template_html,
#                            output_key="html_code")

# prompt_html_chain = SequentialChain(
#     chains=[prompt_chain, code_html_chain],
#     input_variables=['transcription'],
#     output_variables=['html_code', 'prompt']
# )

# result_htm = prompt_html_chain({"transcription": transcription})

# # got html code
# html_code = result_htm["html_code"]


# p_template_css = PromptTemplate(
#     input_variables=['html_code', 'prompt'],
#     template="create me an css code for the following website: {prompt}. The css code is required to be added to this html file:{html_code}. Make sure the css styling applied is in sync with the website description. Only return the css code and nothing else."

# )

# code_css_chain = LLMChain(llm=llm, prompt=p_template_css,
#                           output_key="css_code")

# prompt_css_chain = SequentialChain(
#     chains=[prompt_html_chain, code_css_chain],
#     input_variables=['transcription'],  # Start with transcription
#     output_variables=['css_code', 'html_code', 'prompt']
# )
# result = prompt_css_chain({"transcription": transcription})

# # Extract the CSS code from the result
# css_code = result["css_code"]


# p_template_js = PromptTemplate(
#     input_variables=['prompt', 'html_code', 'css_code'],
#     template="Based on the website description: {prompt}, the HTML code: {html_code}, and the CSS code: {css_code}, create the necessary JavaScript code to add dynamic functionality to the website. Only return the JavaScript code and nothing else."
# )

# # Create an LLMChain for generating JavaScript code
# code_js_chain = LLMChain(llm=llm, prompt=p_template_js, output_key="js_code")

# # Define a SequentialChain that combines the existing chains with the new JavaScript LLMChain
# prompt_javascript_chain = SequentialChain(
#     chains=[prompt_html_chain, code_css_chain, code_js_chain],
#     input_variables=['transcription'],  # Start with transcription
#     output_variables=['js_code', 'css_code', 'html_code', 'prompt']
# )

# # Execute the prompt_javascript_chain with transcription as the input
# result_js = prompt_javascript_chain({"transcription": transcription})

# # Extract the JavaScript code from the result
# js_code = result_js["js_code"]


# # chain = SequentialChain(
# #     chains=[prompt_chain, code_html_chain],
# #     input_variables=['transcription'],
# #     output_variables=['code']
# # )

# # x = chain({'transcription': transcription})
# # print('\n\n\n\n', x)

# with open('output.html', 'w') as f:
#     f.write(html_code)
# with open('output.css', 'w') as f:
#     f.write(css_code)
# with open('output.js', 'w') as f:
#     f.write(js_code)
