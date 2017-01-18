import json
from django_logging_dlp.handlers import ConsoleHandler
from django_logging_dlp.log_object import (LogObject,
                                           ErrorLogObject,
                                           SqlLogObject)

stream_records = []

class StreamMockHandler(ConsoleHandler):

    @classmethod
    def reset(cls):
        global stream_records
        stream_records = []

    @classmethod
    def get_records(cls):
        return stream_records

    def emit(self, record):
        req = record.msg.format_request()
        res = record.msg.format_response()
        rec = dict(request=req, response=res)
        global stream_records
        stream_records.append(rec)
        super(StreamMockHandler, self).emit(record)

    def format(self, record):
        # now just do something a little different so we can see the formatter working
        # visually, there is no test code for this
        if isinstance(record.msg, LogObject) or isinstance(record.msg, SqlLogObject):
            created = int(record.created)
            if isinstance(record.msg, LogObject):
                delta = record.msg.delta
                message = {record.levelname: {delta: {created: record.msg.to_dict}}}
            else:
                message = {record.levelname: {created: record.msg.to_dict}}

            indent = 5
            return json.dumps(message,
                              sort_keys=True,
                              indent=indent)
        elif isinstance(record.msg, ErrorLogObject):
            return str(record.msg)
        elif isinstance(record.msg, dict):
            created = int(record.created)
            message = {record.levelname: {created: record.msg}}
            return json.dumps(message, sort_keys=True, indent=2)
        else:
            return super(ConsoleHandler, self).format(record)
