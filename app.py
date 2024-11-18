import streamlit as st
import google.generativeai as genai

f = open("keys/gemini.txt")
key = f.read()
genai.configure(api_key=key)

sys_prompt = """You are an advanced AI in Python code review and debugging. 
You will receive Python code as input, which may sometimes be incomplete, invalid, or syntactically incorrect. 
Your tasks are: 
1. Analyze the code and identify any syntax or logical errors.
2. If the code is incomplete or invalid, attempt to fix it by assuming the most likely intent of the user.
3. Provide clear and detailed feedback about the issues and your reasoning behind any assumptions you make.
4. Always include a corrected and improved version of the code, even if the input is invalid or broken.

If you cannot make assumptions about the intent due to severely incomplete code, politely inform the user that more context is required."""

model= genai.GenerativeModel(model_name="models/gemini-1.5-flash", system_instruction=sys_prompt)



# Custom CSS for styling
st.markdown(
    """
    <style>
    /* App background */
    .stApp{
        background-image: url("https://images.unsplash.com/photo-1533628635777-112b2239b1c7?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-attachment: fixed;
       
    }
    /* Title styling */
    h1 {
        color: #ffffff;
        font-size: 3rem;
        text-shadow: 2px 2px 5px #000000;
        text-align: center;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1e3d59;
        color: white;
    }
    .sidebar-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sidebar-description {
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐛 PyFix AI")

# Sidebar Section
with st.sidebar:
    st.markdown("<div class='sidebar-title'>About the App</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='sidebar-description'>
        Welcome to the **PyFix AI**, your personal AI-powered coding assistant!  
        
        ✨ **What can this app do?**  
        - Analyze your Python code for potential issues.  
        - Provide detailed feedback and suggestions.  
        - Offer an improved version of your code for better performance and readability.  

        💡 **Why use this app?**  
        - Saves time in debugging and improving code.  
        - Great for beginners and professionals alike.  

        </div>
        """,
        unsafe_allow_html=True
    )
    # st.image("assets/unsplash.jpg", caption="AI-powered Coding Made Simple")

user_code= st.text_area("Enter your Python code here:", height=300, placeholder="Paste or type your Python code...")

btn_review= st.button("🔍Review Code")

# def gemini_review_code(code):
#     try:
#         response = model.generate_content(f"Code to review:\n")
#         return response.text.strip()
#     except Exception as e:
#         return f"An error occurred:{e}"

if btn_review:
    if user_code.strip == "":
        st.warning("Please enter some Python code to review")
    else:
        with st.spinner("Reviewing code..."):
            # feedback = gemini_review_code(user_code)
            response = model.generate_content(f"Code to review:\n{user_code}")
            feedback= response.text.strip()
            st.write("🔍 AI Feedback and Suggestions:")
            st.markdown(f"<div style='background-color:#f9f9f9;padding:10px;border-radius:5px;border-left:5px solid #2196F3;'>{feedback}</div>", unsafe_allow_html=True)

        #Display fixed code in code block
        if "Fixed Code:" in feedback:
            st.write("📝 Suggested Fixed Code:")
            fixed_code = feedback.split("Fixed Code:")[1].strip()
            st.code(fixed_code, language="python")


st.markdown("""
    **Note**: Always review suggested fixes for accuracy and ensure they align with your project’s requirements.
""")