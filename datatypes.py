from typing import NewType
from enum import Enum

SubmitId = NewType('SubmitId', str)
StudentId = NewType('StudentId', str)
EvalId = NewType('EvalId', int)


class WorkerStatus(Enum):
    submitting = 0  # 提交中
    submit_complete = 1  # 提交完成
    submit_failed = 2  # 提交失败
    compiling = 10  # 编译中
    compile_complete = 11  # 编译完成
    compile_failed = 12  # 编译失败
    run_failed = 22  # 运行失败
    testing = 30  # 测试中
    test_complete = 31  # 测试完成
    test_failed = 32  # 测试失败
    detached = 99  # 结束
