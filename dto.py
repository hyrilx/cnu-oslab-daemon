from dataclasses import dataclass

from datatypes import *

@dataclass
class SubmitResponse:
    student_id: StudentId
    eval_id: EvalId
    submit_id: SubmitId
    title: str

@dataclass
class QueryStatusRequest:
    submit_id: SubmitId

@dataclass
class QueryStatusResponse:
    submit_id: SubmitId
    status: WorkerStatus

@dataclass
class QueryEvalPointRequest:
    submit_id: SubmitId

@dataclass
class QueryEvalPointResponse:
    submit_id: SubmitId
    index: int
    brief: str | None
    is_passed: bool
    failed_message: str | None
