from setuptools import setup

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['streamlit', 'openai', 'pytesseract', 'pandas', 'PIL'],
    'includes': ['menu_to_sheet_app.ocr_processor', 'menu_to_sheet_app.gpt_formatter', 'menu_to_sheet_app.sheet_exporter']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)