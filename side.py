import math
import sys


def _check_line(line):
    """
    Checks whether the given line can be solved
    :param line: dict
    :return: bool
    """

    if line['type'] == 'ridge' or line['type'] == 'ending':

        if line['length_real'] != 'null':
            return True
        if line['angle'] != 'null':
            return True
        for point in line['points']:
            if point['z'] != 'null':
                return True
        return False


def check_lines(lines, checked_lines):
    """
    Returns a list of ids of lines that can be solved
    :param lines: list
    :return: list
    """

    valide_lines = []

    for line in lines:
        if line['id'] not in checked_lines and _check_line(line):
            valide_lines.append(line['id'])
    return valide_lines


def solve_line(line):
    """
    Solves the given line(finds real and plan length, angle and coords of top)
    :param line: dict
    :return: dict
    """

    if line['type'] == 'ridge' or line['type'] == 'ending':

        line['length_plan'] = math.sqrt(math.pow(line['points'][0]['x'] - line['points'][1]['x'], 2) + \
                                        math.pow(line['points'][0]['y'] - line['points'][1]['y'], 2))

        if line['angle'] != 'null':
            line['length_real'] = line['length_plan'] / math.cos(math.radians(line['angle']))

            for point in line['points']:
                if point['z'] == 'null':
                    point['z'] = line['length_plan']  * math.tan(math.radians(line['angle']))

        elif line['length_real'] != 'null':
            line['angle'] = math.degrees(math.acos(line['length_plan'] / line['length_real']))

            for point in line['points']:
                if point['z'] == 'null':
                    point['z'] = line['length_plan']  * math.tan(math.radians(line['angle']))
        elif line['points'][0]['z'] != 'null':

            line['angle'] = math.degrees(math.atan(line['points'][0]['z'] / line['length_plan']))
            line['length_real'] = line['length_plan'] / math.cos(math.radians(line['angle']))
        elif line['points'][1]['z'] != 'null':

            line['angle'] = math.degrees(math.atan(line['points'][1]['z'] / line['length_plan']))
            line['length_real'] = line['length_plan'] / math.cos(math.radians(line['angle']))

    elif line['type'] == 'base':

        line['length_plan'] = math.sqrt(math.pow(line['points'][0]['x'] - line['points'][1]['x'], 2) + \
                                        math.pow(line['points'][0]['y'] - line['points'][1]['y'], 2))

        line['length_real'] = line['length_plan']

    elif line['type'] == 'cornice':

        line['length_plan'] = math.sqrt(math.pow(line['points'][0]['x'] - line['points'][1]['x'], 2) + \
                                        math.pow(line['points'][0]['y'] - line['points'][1]['y']), 2)

    elif line['type'] == 'technical_line':
        line['length_plan'] = math.sqrt(math.pow(line['points'][0]['x'] - line['points'][1]['x'], 2) + \
                                        math.pow(line['points'][0]['y'] - line['points'][1]['y'], 2))

        if line['points'][0]['z'] != 'null':

            line['angle'] = math.degrees(math.atan(line['points'][0]['z'] / line['length_plan']))
            line['length_real'] = line['length_plan'] / math.cos(math.radians(line['angle']))
        elif line['points'][1]['z'] != 'null':

            line['angle'] = math.degrees(math.atan(line['points'][1]['z'] / line['length_plan']))
            line['length_real'] = line['length_plan'] / math.cos(math.radians(line['angle']))

    return line


def find_line_crossing(line, lines):
    """
    Returns list of lines` ids that cross with the given one
    :param line: dict
    :param lines: list
    :return: list
    """

    pass



"""
For test purpose
"""
if __name__ == '__main__':

    lines = []

    line = {
        'id': 2,
        'angle': 'null',
        'points': [
            {
                'id': 3,
                'x': 1,
                'y': 5,
                'z': 'null',
            },
            {
                'id': 4,
                'x': 3,
                'y': 7,
                'z': 4,
            },
        ],
        'type': 'ridge',
        'length_plan': 'null',
        'length_real': 'null',
    }

    lines.append(line)

    print(check_lines(lines, []))
