


class Job():
    """
    This is the base class for all jobs to take to standaize them.
    """
    def __init__(self) -> None:
        pass

    def runJob(self):
        raise NotImplementedError
