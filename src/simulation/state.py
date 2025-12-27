from pydantic import BaseModel
from typing import List

class SimluationState:
    def __init__(self):
        self.step = 0
        self.variables = {}
        self.call_stack = []
        self.last_operation = None
        self.issues = {}