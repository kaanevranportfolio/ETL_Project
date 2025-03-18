# ETL Project

This project analyzes cargo ship data, providing insights into various attributes such as ship types, sizes, and construction trends. The project includes an ETL pipeline that processes the data and generates visualizations.

## Project Structure

- **data/**: Contains the CSV file with ship data and generated visualizations.
- **postgresql/**: Contains database-related configurations and scripts.
- **python/**: Contains the ETL script and related Python files.
- **docker-compose.yml**: Configuration for running the project using Docker.

## Dataset

The dataset includes the following attributes for each ship:

- **Company_Name**: The ship's private name.
- **Ship_Name**: Name of the ship.
- **Built_Year**: Year the ship was built.
- **GT (Gross Tonnage)**: A measure of the ship's overall internal volume.
- **DWT (Deadweight Tonnage)**: Maximum weight a ship can safely carry.
- **Length**: Length of the ship.
- **Width**: Width of the ship.

## Visualizations

The project generates several visualizations, including:

1. **Distribution of Ship Types**: Pie chart.
   ![Ship Types](data/ship_type_pie.png)

2. **Distribution of Ship Built Years**: Histogram.
   ![Ship Built Years](data/ship_built_year_hist.png)

3. **Gross Tonnage vs. Deadweight Tonnage**: Scatter plot.
   ![GT vs DWT](data/gt_vs_dwt_scatter.png)

4. **Distribution of Ship Sizes**: Box plot.
   ![Ship Sizes](data/ship_size_box.png)

5. **Yearly Ship Construction Trends**: Line chart.
   ![Yearly Trends](data/yearly_trends_line.png)

6. **Top 10 Longest Ships by Length**: Bar chart.
   ![Longest Ships](data/longest_ships_length.png)

## Setup and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ETL_Project.git
   cd ETL_Project

### Key Points

- **`docker-compose up --build`:** Builds and starts the containers, ensuring any changes are applied.
- The Analysis results are populated in data directory which is on host machine in the same directory wiyh yaml file. (pgdata needs root access to view the files because it is a database)
