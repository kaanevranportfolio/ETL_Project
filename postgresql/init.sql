-- Create a table for storing ship data
CREATE TABLE IF NOT EXISTS ships (
    "Company_Name" VARCHAR(255),
    "Ship_Name" VARCHAR(255),
    "Built_Year" INTEGER,
    "GT" INTEGER,  -- Gross Tonnage
    "DWT" INTEGER,  -- Deadweight Tonnage
    "Length" FLOAT,
    "Width" FLOAT
);