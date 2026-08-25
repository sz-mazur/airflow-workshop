from dataclasses import dataclass


@dataclass(frozen=True)
class WorkshopConfig:
    URL_AIRFLOW_UI: str = "http://localhost:8080/"
    API_PATH: str = "api/v1/"
    URL_AIRFLOW_API: str = URL_AIRFLOW_UI + API_PATH
    AIRFLOW_USER: str = "airflow"
    AIRFLOW_PASSWORD: str = "airflow"
    OUTPUT_PATH: str = "/opt/airflow/dags/output/"
    AUTH: tuple[str, str] = (AIRFLOW_USER, AIRFLOW_PASSWORD)
