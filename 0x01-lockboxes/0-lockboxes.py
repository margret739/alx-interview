#!/usr/bin/python3
"""solves the the lockboxes puzzle"""


def look_next_opened_box(opened_boxes):
    """looks for the next opened box
    Args:
        opened_boxes (dict): dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the box"""

    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """check if all boxes can be opened
    Args:
        boxes (list): list which contain all the boxes with the keys
    returns:
        bool: true if all boxes can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                    'status': 'opened',
                    'keys': boxes[0],
            }
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    aux[key] = {
                            'status': 'opened',
                            'keys': boxes[key]
                    }
                except (keyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
