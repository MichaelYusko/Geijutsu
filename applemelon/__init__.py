from werkzeug.serving import run_simple


class AppleMelon:
    def __init__(self):
        pass

    def run(self, host='localhost', port=5000, debug=True):
        return run_simple(host, port, self, debug)
