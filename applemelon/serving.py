from werkzeug.serving import run_simple


def _run_server(host: str='127.0.0.1', port: int=5000, debug: bool=False):
    return run_simple(host, port, debug)
