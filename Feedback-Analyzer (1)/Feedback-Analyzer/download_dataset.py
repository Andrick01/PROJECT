
from datasets import load_dataset
import pandas as pd
from pathlib import Path

# Load the DAIR.AI emotion dataset
print("Downloading the DAIR.AI emotion dataset...")

dataset = load_dataset("dair-ai/emotion", "split")

# Create the data folder
data_dir = Path("data/raw")
data_dir.mkdir(parents=True, exist_ok=True)

# Display available dataset splits
print("\nDataset splits:")
print(dataset)

# Convert each split into a CSV file
for split_name, split_data in dataset.items():
    df = split_data.to_pandas()

    output_path = data_dir / f"{split_name}.csv"
    df.to_csv(output_path, index=False)

    print(f"\nSaved: {output_path}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")

# Display example records
print("\nSample training records:")
print(dataset["train"].to_pandas().head())

# Display the emotion labels
print("\nEmotion label mapping:")
print(dataset["train"].features["label"].names)

print("\nDataset download and inspection completed!")
