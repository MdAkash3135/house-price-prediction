from zenml import pipeline, Model, step


@pipeline(
    model=Model(name="house_price_prediction_model"),
)
def ml_pipeline():
    """A pipeline for training a machine learning model."""
    pass