from geijutsu.serving import _run_server


class Geijutsu:
    """
    Main class
    """
    def run(self, host: str='127.0.0.1', port: int=5000, debug: bool=False):
        return _run_server(host, port, debug)
