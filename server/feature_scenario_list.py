import os


def list_scenarios(directory):
    features = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".feature"):
                feature_path = os.path.join(root, file)
                with open(feature_path, "r") as f:
                    feature_name = None
                    scenarios = []
                    for line in f:
                        line = line.strip()
                        if line.startswith("Feature:"):
                            feature_name = line[len("Feature:") :].strip()  # noqa
                        elif line.startswith("Scenario:") or line.startswith(
                            "Scenario Outline:"
                        ):
                            scenario_name = line.split(":", 1)[1].strip()
                            scenarios.append(scenario_name)
                    if feature_name:
                        features[feature_name] = (
                            features.get(feature_name, []) + scenarios
                        )

    for feature, scenarios in features.items():
        print(f"Feature: {feature}")
        for scenario in scenarios:
            print(f"  - Scenario: {scenario}")


directory = "./"
list_scenarios(directory)
