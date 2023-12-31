# MedAI - Early stage diabetes risk prediction

---

## Dataset

### Source

This dataset is originally from <a href="https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.#">UCI Machine Learning Repository</a>. It contains the sign and symptom data of newly diabetic or would be diabetic patient. This has been col-
lected using direct questionnaires from the patients of Sylhet Diabetes
Hospital in Sylhet, Bangladesh and approved by a doctor.

### Attribute Information

- Age 1.20-65
- Sex 1. Male, 2.Female
- Polyuria 1.Yes, 2.No.
- Polydipsia 1.Yes, 2.No.
- sudden weight loss 1.Yes, 2.No.
- weakness 1.Yes, 2.No.
- Polyphagia 1.Yes, 2.No.
- Genital thrush 1.Yes, 2.No.
- visual blurring 1.Yes, 2.No.
- Itching 1.Yes, 2.No.
- Irritability 1.Yes, 2.No.
- delayed healing 1.Yes, 2.No.
- partial paresis 1.Yes, 2.No.
- muscle stiffness 1.Yes, 2.No.
- Alopecia 1.Yes, 2.No.
- Obesity 1.Yes, 2.No.
- Class 1.Positive, 2.Negative.

## USAGE

Dockers are used to run the application. To run the application, you need to install docker. Then, you can run the application with the following command:

```bash
docker build -t <image-name> .
docker run -p 8000:8000 -v models:/app/models <image-name>
```

### APIs Documentation

The application exposes the following APIs:

- POST /predict
- URL: http://localhost:8000/predict
- Body Request
```
{
    "age": 30,
    "gender": "Male",
    "polyuria": 1,
    "polydipsia": 0,
    "sudden_weight_loss": 1,
    "weakness": 0,
    "polyphagia": 1,
    "genital_thrush": 0,
    "visual_blurring": 1,
    "itching": 0,
    "irritability": 1,
    "delayed_healing": 0,
    "partial_paresis": 1,
    "muscle_stiffness": 0,
    "alopecia": 1
}
```
- Response
```
{
  "message": "It is predicted that this patient has diabetes.",
  "status": 1
}
```

@TODO add more information about the models, the training process, and the results.
