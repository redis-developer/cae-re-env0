import json


def remove_duplicates(json_obj):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == "enum" and isinstance(value, list):
                json_obj[key] = list(set(value))
            else:
                remove_duplicates(value)
    elif isinstance(json_obj, list):
        for item in json_obj:
            remove_duplicates(item)


if __name__ == "__main__":
    with open("env0_spec.json", "r") as f:
        openapi = json.load(f)
    remove_duplicates(openapi)
    with open("env0_spec_fixed.json", "w") as f:
        json.dump(openapi, f, indent=4)
