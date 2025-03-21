import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_data(file_path):
    """Read the CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)

def transform_data(df):
    """Transform the data as needed."""
    df.columns = [
        'Company_Name', 'Ship_Name', 'Built_Year', 'GT', 'DWT', 'Length', 'Width'
    ]
    return df

def load_data(df, table_name='ships'):
    """Load the DataFrame into a PostgreSQL database."""
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data loaded into table {table_name} successfully.")

def visualize_data(engine, output_dir="data"):
    """Visualize the data from the database and save as PNG."""
    # Query the data
    query = "SELECT * FROM ships"
    df = pd.read_sql(query, engine)

    # Pie Chart for Ship Type Distribution
    ship_types = df['Ship_Name'].value_counts()
    plt.figure(figsize=(10, 10))
    ship_types.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='tab20')
    plt.title('Distribution of Ship Types', fontsize=16)
    plt.ylabel('')  # Hide y-label for a cleaner look
    output_path_pie = os.path.join(output_dir, "ship_type_pie.png")
    plt.tight_layout()
    plt.savefig(output_path_pie)
    print(f"Pie chart saved to {output_path_pie}")
    plt.close()

    # Histogram for Ship Age Distribution
    plt.figure(figsize=(12, 8))
    df['Built_Year'].plot(kind='hist', bins=20, color='lightgreen')
    plt.title('Distribution of Ship Built Year', fontsize=16)
    plt.xlabel('Built Year', fontsize=14)
    plt.ylabel('Number of Ships', fontsize=14)
    plt.tight_layout()
    output_path_hist = os.path.join(output_dir, "ship_built_year_hist.png")
    plt.savefig(output_path_hist)
    print(f"Histogram saved to {output_path_hist}")
    plt.close()

    # Scatter Plot for GT vs. DWT
    plt.figure(figsize=(12, 8))
    plt.scatter(df['GT'], df['DWT'], alpha=0.5, color='purple')
    plt.title('Gross Tonnage vs. Deadweight Tonnage', fontsize=16)
    plt.xlabel('Gross Tonnage (GT)', fontsize=14)
    plt.ylabel('Deadweight Tonnage (DWT)', fontsize=14)
    plt.tight_layout()
    output_path_scatter = os.path.join(output_dir, "gt_vs_dwt_scatter.png")
    plt.savefig(output_path_scatter)
    print(f"Scatter plot saved to {output_path_scatter}")
    plt.close()

    # Box Plot for Ship Size (Length and Width)
    plt.figure(figsize=(12, 8))
    df[['Length', 'Width']].plot(kind='box', color=dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray'))
    plt.title('Distribution of Ship Sizes', fontsize=16)
    plt.ylabel('Size (meters)', fontsize=14)
    plt.tight_layout()
    output_path_box = os.path.join(output_dir, "ship_size_box.png")
    plt.savefig(output_path_box)
    print(f"Box plot saved to {output_path_box}")
    plt.close()

    # Line Chart for Yearly Ship Construction Trends
    yearly_trends = df['Built_Year'].value_counts().sort_index()
    plt.figure(figsize=(12, 8))
    yearly_trends.plot(kind='line', color='orange')
    plt.title('Yearly Ship Construction Trends', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Ships Built', fontsize=14)
    plt.tight_layout()
    output_path_line = os.path.join(output_dir, "yearly_trends_line.png")
    plt.savefig(output_path_line)
    print(f"Line chart saved to {output_path_line}")
    plt.close()

    # Bar Chart for Top 10 Longest Ships with Company Name
    top_ships_length = df.nlargest(10, 'Length')
    plt.figure(figsize=(12, 8))
    labels = top_ships_length.apply(lambda row: f"{row['Ship_Name']} ({row['Company_Name']})", axis=1)
    plt.bar(labels, top_ships_length['Length'], color=[cm.get_cmap('tab10')(i) for i in range(10)])
    plt.title('Top 10 Longest Ships by Length', fontsize=16)
    plt.xlabel('Ship Name (Company)', fontsize=14)
    plt.ylabel('Length (meters)', fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    output_path_length = os.path.join(output_dir, "longest_ships_length.png")
    plt.savefig(output_path_length)
    print(f"Bar chart saved to {output_path_length}")
    plt.close()

if __name__ == "__main__":
    # Path to the CSV file in your folder
    csv_path = 'data/ship_data.csv'

    # Extract, transform, and load the data
    data = extract_data(csv_path)
    transformed_data = transform_data(data)
    load_data(transformed_data)

    # Create a database engine for visualization
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)

    # Visualize the data
    visualize_data(engine)