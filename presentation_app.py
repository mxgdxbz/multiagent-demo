import streamlit as st
import streamlit.components.v1 as components
import os
import openai  # Assuming you're using OpenAI, replace with your desired LLM library
import time  # For simulating typing effect


# --- CONFIGURATION ---
# OpenAI API Key (replace with your actual key, preferably using st.secrets)
# You can set the API key in streamlit secrets (Settings -> Secrets)
# then access it as: openai.api_key = st.secrets["OPENAI_API_KEY"]

openai.api_key = "YOUR_OPENAI_API_KEY"  #  **REPLACE WITH YOUR OPENAI API KEY**
MODEL_NAME = "gpt-3.5-turbo"  # Or your preferred model



# --- HELPER FUNCTIONS ---

def load_presentation(file_path):
    """Loads the HTML content of a reveal.js presentation."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def generate_llm_response(prompt):
    """Generates a response from the LLM."""
    try:
        completion = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {e}"

def render_typed_text(text, delay=0.02):
    """Renders text with a typing effect."""
    container = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        container.markdown(full_text)
        time.sleep(delay)


# --- STREAMLIT APP ---

st.title("Interactive Presentation with LLM Chat")

# --- SIDEBAR ---
st.sidebar.header("Configuration")
presentation_file = st.sidebar.file_uploader("Upload your reveal.js presentation (HTML file)", type=["html"])
if presentation_file is None:
    st.sidebar.warning("Please upload your reveal.js presentation HTML file.")
    presentation_file_path = "example_presentation.html"  # Default presentation filename
    # Create an example_presentation.html if it doesn't exist
    if not os.path.exists(presentation_file_path):
        with open(presentation_file_path, "w") as f:
            f.write("""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
                <title>Reveal.js Presentation</title>
                <link rel="stylesheet" href="https://revealjs.com/css/reveal.css">
                <link rel="stylesheet" href="https://revealjs.com/css/theme/black.css">
                <link rel="stylesheet" href="https://revealjs.com/lib/css/zenburn.css">
                <script>
                    var link = document.createElement( 'link' );
                    link.rel = 'stylesheet';
                    link.type = 'text/css';
                    link.href = window.location.search.match( /print-pdf/gi ) ? 'https://revealjs.com/css/print/pdf.css' : 'https://revealjs.com/css/print/paper.css';
                    document.getElementsByTagName( 'head' )[0].appendChild( link );
                </script>
            </head>
            <body>
                <div class="reveal">
                    <div class="slides">
                        <section><h1>Welcome to Reveal.js!</h1>
                           <p>This is a sample presentation.</p>
                        </section>
                        <section>
                            <h2>Slide 2</h2>
                            <p>Content for the second slide.</p>
                        </section>
                    </div>
                </div>

                <script src="https://revealjs.com/js/reveal.js"></script>
                <script>
                    Reveal.initialize({
                        dependencies: [
                            { src: 'https://revealjs.com/lib/js/classList.js', condition: function() { return !document.body.classList; } },
                            { src: 'https://revealjs.com/plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                            { src: 'https://revealjs.com/plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                            { src: 'https://revealjs.com/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
                            { src: 'https://revealjs.com/plugin/zoom-js/zoom.js', async: true },
                            { src: 'https://revealjs.com/plugin/notes/notes.js', async: true },
                            { src: 'https://revealjs.com/plugin/math/math.js', async: true }
                        ]
                    });
                </script>
            </body>
            </html>
            """)

    # Load default presentation
    with open(presentation_file_path, "r", encoding="utf-8") as f:
        presentation_html = f.read()
else:
    presentation_html = presentation_file.read().decode("utf-8")

# --- PRESENTATION DISPLAY ---

st.header("Presentation")
components.html(presentation_html, height=600, scrolling=False)


# --- LLM CHAT ---

st.header("LLM Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a question about the presentation or any topic..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display LLM response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            full_response = generate_llm_response(prompt)
            #st.markdown(full_response)  #Original
            render_typed_text(full_response) #Typed Response

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})