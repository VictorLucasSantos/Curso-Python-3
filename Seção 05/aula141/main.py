from log import LogFileMixin, LogPrintMixin

l = LogPrintMixin()
l.log_error("qualquer coisa")
l.log_success("top")
lf = LogFileMixin()
lf.log_error("qualquer")
lf.log_success("coisa")
