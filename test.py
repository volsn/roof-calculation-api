import extras
import side


def parse_lines(shapes):

    lines = extras.exact_lines(shapes) # a dict containing information about all the lines
    lines_to_check = [] # list of lines that are about to be solved
    checked_lines = [] # list of lines that are already solved

    lines_to_check = side.check_lines(lines, checked_lines)

    while lines_to_check is not []:

        for id in lines_to_check:
            i = extras.find_element_by_id(lines, id)
            checked_line = side.solve_line(lines[i])
            checked_lines.append(id)

            lines[i] = checked_line

            # Set values of points of the checked lines to lines that cross with it
            for point in checked_line['points']:

                for line_ in lines:
                    if line_['id'] not in checked_lines:
                        for point_ in line_['points']:
                            if point_['id'] == point['id']:
                                point_ = point

            del(id)

        lines_to_check = side.check_lines(lines, checked_lines)



"""
For test purpose
"""
if __name__ == '__main__':