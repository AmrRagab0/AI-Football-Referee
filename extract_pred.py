import json

# Load the predictions from results_spotting file
with open("results_spotting.json", 'r') as f:
    data = json.load(f)
    predictions = data["predictions"]

# Sort the predictions by confidence in descending order
sorted_predictions = sorted(predictions, key=lambda x: float(x["confidence"]), reverse=True)

# Write the top 5 predictions with the highest confidence to a file
with open("top_predictions.txt", "w") as f:
    for i, pred in enumerate(sorted_predictions[:40]):
        f.write(f"Prediction {i+1}:\n")
        f.write(f"  Label: {pred['label']}\n")
        f.write(f"  Confidence: {pred['confidence']}\n")
        f.write(f"  Game time: {pred['gameTime']}\n")
        f.write(f"  Position: {pred['position']}\n")
        f.write(f"  Half: {pred['half']}\n\n")
