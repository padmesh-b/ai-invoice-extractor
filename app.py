from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
from google import genai   # ✅ NEW SDK

# Create client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -------- Gemini Function -------- #
def get_gemini_response(system_prompt, image, user_question):

    # Convert image to bytes
    import io
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="PNG")
    img_bytes = img_byte_arr.getvalue()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            system_prompt,
            {"mime_type": "image/png", "data": img_bytes},  # ✅ correct format
            user_question
        ],
    )

    return response.text


# -------- Streamlit UI -------- #

st.set_page_config(page_title="Invoice Extractor")
st.header("📄 Gemini Invoice Understanding App")

user_input = st.text_input("Ask something about the invoice:")

uploaded_file = st.file_uploader(
    "Upload invoice image",
    type=["jpg", "jpeg", "png"]
)

image = None

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_container_width=True)

submit = st.button("Analyze Invoice")

system_prompt = """
You are an expert in understanding invoices.
Answer questions only based on the uploaded invoice.
If information is missing, say 'Not found in invoice'.
"""

if submit:
    if image is None:
        st.warning("Please upload an invoice image.")
    else:
        with st.spinner("Analyzing invoice..."):
            response = get_gemini_response(
                system_prompt,
                image,
                user_input if user_input else "Summarize this invoice"
            )

        st.subheader("Response:")
        st.write(response)