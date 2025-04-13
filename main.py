import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def export_envs(environment: str = "dev") -> None:
    env_file = f"config/.env.{environment}"
    if not os.path.exists(env_file):
        raise FileNotFoundError(f"{env_file} not found")
    load_dotenv(dotenv_path=env_file, override=True)

    # Debug print
    print("DEBUG ENVIRONMENT:", os.environ.get("ENVIRONMENT"))
    print("DEBUG APP_NAME:", os.environ.get("APP_NAME"))


# Load secrets.yaml and export as environment variables
with open("secrets.yaml", "r") as f:
    secrets = yaml.safe_load(f)
    for key, value in secrets.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("FAKE_API_KEY:", settings.FAKE_API_KEY)
