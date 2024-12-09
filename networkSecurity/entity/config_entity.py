from datetime import datetime
import os
from networkSecurity.components import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now):
        timestamp = timestamp.strftime('%m_%d_%y_%H_%M_%S')
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.time_stamp: str = timestamp