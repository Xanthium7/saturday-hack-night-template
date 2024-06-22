
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


# print(transcription)
# transcription = "create me a single page cool resturant website with navbar each food listing"


# llm = OpenAI(model_name="gpt-4o", temperature=0.6)
llm = ChatOpenAI()


# print("\n\n\n", prompt)


def generate_html_sections(prompt):

    section_prompt = f"Generate the  HTML code for a page based on: {prompt}. Include necessary classes and ids for each element. The html should include link section linking 'output.css' in same folder and script linking 'output.js' in same folder.  Exclude the css code and javascript code. Give back the html code as plain text (make sure the response does not contain ' ``` ' tag). (if at any point,any images are needed to be added then use 'https://placehold.co/600x400' as the image source)"
    p_template_html_section = PromptTemplate(
        input_variables=['transcription'],
        template=section_prompt
    )
    code_html_chain_section = LLMChain(
        llm=llm, prompt=p_template_html_section, output_key="html_code_section")
    result_section = code_html_chain_section(
        {"transcription": prompt})
    html_section = result_section["html_code_section"]
    return html_section


def sanitize_for_format(string):
    # Replace single curly braces with doubled curly braces to escape them
    return string.replace("{", "").replace("}", "")


def generate_css_sections(prompt, html_code):

    sanitized_prompt = sanitize_for_format(prompt)
    sanitized_html_code = sanitize_for_format(html_code)

    section_prompt = f"Create the CSS code stylings based on the website description: {sanitized_prompt} and the HTML code: {sanitized_html_code}. Give only the css code as plain text (make sure the response does not contain ' ``` ' tag). use proper classes or ids as used in the html code"

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

    return css_section


def generate_js_sections(prompt, html_code):

    sanitized_prompt = sanitize_for_format(prompt)
    sanitized_html_code = sanitize_for_format(html_code)
    # Modify the prompt to request a specific section of the JavaScript
    section_prompt = f"Create the JavaScript code based on the website description: {sanitized_prompt}, the HTML code: {sanitized_html_code}. Give only the javascript code as plain text (make sure the response does not contain ' ``` ' tag) and nothing else"
    p_template_js_section = PromptTemplate(
        input_variables=['prompt', 'html_code'],
        template=section_prompt
    )
    code_js_chain_section = LLMChain(
        llm=llm, prompt=p_template_js_section, output_key="js_code_section")
    result_section = code_js_chain_section(
        {"prompt": prompt, "html_code": html_code})
    js_section = result_section["js_code_section"]

    return js_section


def output_func(transcription):

    p_template_name = PromptTemplate(
        input_variables=['transcription'],
        template="You are a prompt generating bot that will take an instruction about a website and u will need to describe that website clealrly with a proper color pallete and theme. You should describe the need of any stylings, animations or images that may be required.It should have a default font of Arial, unless specified differently. (You will be giving these instructions to a coding bot that will genrate the html css and js code). Keep the instructions less than 200 words. your given the instruction :{transcription}."

    )
    p_template_name.format(
        transcription=transcription)

    prompt_chain = LLMChain(llm=llm, prompt=p_template_name,
                            output_key="prompt")

    prompt_return = prompt_chain(transcription)
    prompt = prompt_return['prompt']

    html_code = generate_html_sections(prompt)

    # print("\n\n\n", html_code)
    css_code = generate_css_sections(prompt, html_code)

    # print("\n\n\n", css_code)
    js_code = generate_js_sections(prompt, html_code)

    # print("\n\n\n", js_code)

    # Save the generated code to files
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html_code)
    with open('output.css', 'w', encoding='utf-8') as f:
        f.write(css_code)
    with open('output.js', 'w', encoding='utf-8') as f:
        f.write(js_code)