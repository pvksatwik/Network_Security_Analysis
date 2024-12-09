import os, sys

from networkSecurity.components.data_ingestion import DataIngestion
from networkSecurity.components.data_transformation import DataTransformation
from networkSecurity.components.data_validation import DataValidation
from networkSecurity.components.model_evaluation import ModelEvaluation
from networkSecurity.components.model_pusher import ModelPusher
from networkSecurity.components.model_trainer import ModelTrainer

from networkSecurity.exception.exception import NetworkSecurityException

from networkSecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
    ModelTrainerConfig
)

from networkSecurity.entity.artifact_entity import(
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact,
    ModelTrainerArtifact
)

class TrainingPipeline:
    def __init__(self):
        pass
    
    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)