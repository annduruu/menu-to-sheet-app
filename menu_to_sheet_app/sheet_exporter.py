
import pandas as pd

def save_menu_to_excel(menu_data, output_path):
    df = pd.DataFrame(menu_data)
    df.to_excel(output_path, index=False)
