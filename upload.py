from huggingface_hub import HfApi

api = HfApi()

files = [
    "models/model.pkl",
    "models/encoder_sexe.pkl", 
    "models/encoder_region.pkl",
    "models/feature_cols.pkl"
]

for f in files:
    print(f"Upload de {f}...")
    api.upload_file(
        path_or_fileobj=f,
        path_in_repo=f,
        repo_id="twiss00/sensante",
        repo_type="space"
    )
    print(f"OK : {f}")

print("Terminé !")