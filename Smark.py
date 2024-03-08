
import streamlit as st
import google.generativeai as genai

#Use your own api key which u can find from google studio
genai.configure(api_key="")

# Set up the model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 30720,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
]

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.0-pro-001",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

def main():
    st.title("Smark Powered By Gemini ")
    prompt = st.text_area("Enter your prompt:", value="")

    if st.button("Generate Content"):
        prompt_parts = [prompt]
        response = model.generate_content(prompt_parts)
        st.write("Generated Response:")
        for part in response.parts:
            st.write(part.text)

if __name__ == "__main__":
    main()