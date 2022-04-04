import mlflow
import wandb


def log_artifact(
    artifact_name, artifact_type, artifact_description, filename, wandb_run
):
    """logs artifact to wandb

    Args:
        artifact_name (str): Name of artifact to be logged
        artifact_type (str): type of artifact
        artifact_description (str): description of artifact
        filename (str): Name given for file
        wandb_run (str): Run of wandb to be created
    """
    # Log to W&B
    artifact = wandb.Artifact(
        artifact_name,
        type=artifact_type,
        description=artifact_description,
    )
    artifact.add_file(filename)
    wandb_run.log_artifact(artifact)
    artifact.wait()
