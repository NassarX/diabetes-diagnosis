import json
import pandas as pd

def validate_field(field, value, validation_criteria):
    if not value and value != 0:
        return f"Missing {field} field"

    if not validation_criteria(str(value)):
        return f"Invalid {field} value"
    return None


def validate_request(form_data):
    validations = {
        "age": str.isdigit,
        "gender": lambda x: x in ['Male', 'Female'],
        **{field: lambda x: x in ['0', '1'] for field in [
            "polyuria", "polydipsia", "sudden_weight_loss", "weakness",
            "polyphagia", "genital_thrush", "visual_blurring", "itching",
            "irritability", "delayed_healing", "partial_paresis",
            "muscle_stiffness", "alopecia"
        ]}
    }

    for field, validation in validations.items():
        error = validate_field(field, form_data.get(field), validation)
        if error:
            return error
    return None


def preprocess(data):
    updated_data = {}
    for key, value in data.items():
        # Replace underscores with spaces in keys
        updated_key = key.replace('_', ' ')

        # Replace 1 with 'Yes' and 0 with 'No' in values
        updated_value = 'Yes' if value == 1 else 'No' if value == 0 else value

        # Update the dictionary with modified keys and values
        updated_data[updated_key] = updated_value

    return updated_data


def make_prediction(model, inputs):
    data = pd.DataFrame([inputs])
    pred = model.predict(data)[0]
    if pred == 0:
        return {
            "status": 0,
            "message": "It is predicted that this patient does not have diabetes."
        }
    else:
        return {
            "status": 1,
            "message": "It is predicted that this patient has diabetes."
        }
