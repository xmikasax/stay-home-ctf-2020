import math
import random
from checklib import Status

PORT = 5001


class CheckMachine:
    @property
    def url(self):
        return f'http://{self.c.host}:{self.port}'

    def __init__(self, checker):
        self.c = checker
        self.port = PORT

    def telemetry(self, s, idx):
        url = f'{self.url}/telemetry/{idx}'

        response = s.get(url)

        self.c.assert_eq(response.status_code, 200, "GROUND TERMINAL ERROR")

        response_body = self.c.get_json(response, "GROUND TERMINAL ERROR",
                                        Status.MUMBLE)

        if 'error' in response_body or 'object' not in response_body:
            self.c.cquit(Status.MUMBLE, "GROUND TERMINAL ERROR",
                         '/telemetry/ error: ' + response['error'])

        return response_body['object']

    def beam(self, s, idx, angle):
        url = f'{self.url}/beam/{idx}'

        response = s.post(url, json=dict(angle=angle))

        self.c.assert_eq(response.status_code, 200, "RELAY ERROR")

        response_body = self.c.get_json(response, "RELAY ERROR", Status.MUMBLE)

        if 'error' in response_body or 'responses' not in response_body:
            self.c.cquit(Status.MUMBLE, "RELAY ERROR",
                         '/beam/ error: ' + response['error'])

        return ' '.join(response_body['responses'])

    @staticmethod
    def random_angle():
        return round(math.degrees(random.random() * math.pi * 2), 2)

    def launch(self, s, msg, low_orbit):
        url = f'{self.url}/launch/'

        if low_orbit:
            height = random.randint(5000, 10000)
            msg = ''
            af = random.choice([
                0.41,
                0.45,
                0.51,
                0.40,
                0.44,
                0.59,
            ])
        else:
            height = random.randint(20000, 900000)
            af = 0

        response = s.post(url,
                          json=dict(
                              phase=CheckMachine.random_angle(),
                              height=height,
                              antenna_focus=af,
                              narrow_beam_response=msg,
                              mass=100,
                          ))

        self.c.assert_eq(response.status_code, 200, "LAUNCH ABORT")

        response_body = self.c.get_json(response, "LAUNCH ABORT",
                                        Status.MUMBLE)

        if 'error' in response_body:
            self.c.cquit(Status.MUMBLE, "LAUNCH FAILURE",
                         '/launch/ error: ' + response['error'])

        if 'id' not in response_body:
            self.c.cquit(Status.MUMBLE, "LAUNCH FAILURE",
                         '/launch/ error: id not in response')

        idx = response_body['id']

        if 'position' not in response_body or len(
                response_body['position']) != 2:
            self.c.cquit(Status.MUMBLE, "LAUNCH FAILURE",
                         '/launch/ error: position has invalid format')

        pos_x, pos_y = response_body['position']
        pos = (pos_x, pos_y)

        if abs(math.dist((0, 0), pos) - height) > 10:
            self.c.cquit(Status.MUMBLE, "ORBIT NOT REACHED",
                         '/launch/ error: position with invalid height')

        return idx, height, pos_x, pos_y
