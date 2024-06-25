
![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)




# Speak to Site

Transform your web development experience with our LangChain project! Seamlessly create stunning websites using just your voice. Speak to Site turns your website ideas into reality by simply describing what you want. This tool not only generates an interactive website based on your description but also allows you to alter and modify the website if you don't like the initial version. Elevate your design potential with this powerful tool that blends simplicity with functionality, making your web creation process more enjoyable and efficient


## Team Members
1. [Akshhay KM](https://github.com/Xanthium7/saturday-hack-night-template)
2. [Alan Francis Santhosh](https://github.com/alanfrancis442/saturday-hack-night-template)


## How It Works

### Project Architecture
Our project leverages LangChain and Streamlit to provide a seamless web development experience. Below is the architecture that outlines the flow of data and processes within the project:

  <img src="https://github.com/Xanthium7/saturday-hack-night-template/assets/119670162/8a062ac6-01ee-46c7-85e8-82a3a387570c" alt="Project Demo 1" width="500"/>

### Project Demo
1. **Input via Audio**

   - **Step 1**: Users provide input through an audio interface.
   - **Step 2**: The audio input is processed by an initial Language Learning Model (LLM), which converts it into a well-structured prompt.
   <img src="https://github.com/Xanthium7/saturday-hack-night-template/assets/119670162/27357bef-11f2-470f-bc14-7840f16484f3" alt="Project Architecture" width="500"/>

2. **Code Creation and Integration**

   - **Step 3**: The structured prompt is then passed to different LLMs, each specialized in generating HTML, CSS, or JavaScript code.
   - **Step 4**: The generated code segments are then merged by another LLM to form a cohesive and functional codebase.
   <img src="https://github.com/Xanthium7/saturday-hack-night-template/assets/119670162/8a6bdd86-807e-46ee-8f63-aba238e6df17" alt="Project Demo 2" width="500"/>

3. **Website Preview**

   - **Step 5**: Once the code is integrated, a link is generated.
   - **Step 6**: Users can click the link to preview the fully functional website created by the AI.
   <img src="https://github.com/Xanthium7/saturday-hack-night-template/assets/119670162/395214c1-cb6a-479c-a5c8-ad1d2362f64d" alt="Project Demo 3" width="500"/>

## Link to Product Walkthrough


https://github.com/Xanthium7/saturday-hack-night-template/assets/119670162/d2112307-473b-4274-a8fa-c16594dcd2e2


## Libraries Used
Our project utilizes the following libraries to achieve its functionality:
- **LangChain**: 
- **Streamlit**: 

## How to Configure
To set up the project, follow these steps:
1. **Create a `.env` File**:
   - In the root directory of the project, create a file named `.env`.
   - Add the following line to the `.env` file, replacing `your_openai_api_key` with your actual OpenAI API key:
```plaintext
OPENAI_API_KEY=your_openai_api_key
```

## How to Run
To run the project, use the following command:
```sh
streamlit run main.py
