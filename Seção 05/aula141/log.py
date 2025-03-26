# Abstração

from pathlib import Path

# obtendo caminho do local de arquivo
LOG_FILE = Path(__file__).parent / "log.txt"


class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o método log")

    def log_error(self, msg):
        return self._log(f"Error: {msg}")

    def log_success(self, msg):
        return self._log(f"Success: {msg}")


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f"{msg} ({self.__class__.__name__})"
        with open(LOG_FILE, "a") as f:
            print(f"Salvando no log: {msg_formatada}")
            f.write(msg_formatada)
            f.write("\n")


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f"{msg} {self.__class__.__name__}")


if __name__ == "__main__":
    l = LogPrintMixin()
    l.log_error("qualquer coisa")
    l.log_success("top")
    lf = LogFileMixin()
    lf.log_error("qualquer")
    lf.log_success("coisa")
    print(LOG_FILE)
