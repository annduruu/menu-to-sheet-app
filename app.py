
import streamlit as st
from menu_to_sheet_app.ocr_processor import extract_text_from_image
from menu_to_sheet_app.gpt_formatter import format_menu_with_gpt
from menu_to_sheet_app.sheet_exporter import save_menu_to_excel
import tempfile

st.title("Menu to Sheet Converter")

api_key = st.text_input("Enter your OpenAI API key", type="password")
uploaded_file = st.file_uploader("Upload a menu image", type=["jpg", "jpeg", "png"])

if uploaded_file and api_key:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    with st.spinner("Extracting text..."):
        ocr_text = extract_text_from_image(tmp_path)

    with st.spinner("Formatting with GPT..."):
        menu_data = format_menu_with_gpt(ocr_text, api_key)

    output_path = "menu_output.xlsx"
    save_menu_to_excel(menu_data, output_path)

    with open(output_path, "rb") as file:
        btn = st.download_button(
            label="Download Excel File",
            data=file,
            file_name="menu_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
