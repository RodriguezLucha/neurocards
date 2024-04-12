import os


def list_features(directory):
    features = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".feature"):
                feature_path = os.path.join(root, file)
                with open(feature_path, "r") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("Feature:"):
                            feature_name = line[len("Feature:") :].strip()  # noqa
                            features.add(feature_name)
                            break  # only need the feature name

    for feature in sorted(features):
        print(f"Feature: {feature}")


directory = "./"
list_features(directory)
