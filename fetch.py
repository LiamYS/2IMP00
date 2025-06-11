import csv
from huggingface_hub import list_models

models = list_models(cardData=True)
model_data = []

for i, model in enumerate(models):

    card_data = model.card_data or {}
    if type(card_data.get("base_model", [])) is str:
        card_data["base_model"] = card_data["base_model"]
    else:
        card_data["base_model"] = ",".join(card_data.get("base_model", []))

    model_info = {
        "id": model.modelId,
        "likes": model.likes,
        "downloads": model.downloads,
        "created_at": model.created_at.isoformat(),
        "base_model": card_data.get("base_model"),
        "library_name": card_data.get("library_name"),
        "license": card_data.get("license"),
        "pipeline_tag": card_data.get("pipeline_tag"),
    }

    model_data.append(model_info)

    if i % 1000 == 0:
        print("Processed ", i, "models")

with open("models.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=model_data[0].keys(), delimiter="|")
    writer.writeheader()
    writer.writerows(model_data)
