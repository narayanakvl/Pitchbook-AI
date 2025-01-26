import os
import pandas as pd
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_fake_data(rows, columns):
    data = {
        col.strip(): [
            fake.name() if "name" in col.lower() else fake.random_number() 
            for _ in range(rows)
        ]
        for col in columns
    }
    df = pd.DataFrame(data)
    
    # Correctly set the path to `generated_files` relative to the current script
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
    output_dir = os.path.join(base_dir, 'generated_files')  # Append 'generated_files'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save the file
    file_path = os.path.join(output_dir, f'fake_data_{timestamp}.xlsx')  # Full path to the file
    df.to_excel(file_path, index=False)
    return file_path
