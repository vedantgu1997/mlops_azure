import sys, os
from imgSegmentation.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()
print('Training done successfully! ')