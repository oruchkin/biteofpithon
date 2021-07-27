class ThreadData:
    __common_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1,
    }

    def __init__(self):
        self.__dict__ = ThreadData.__common_attrs
