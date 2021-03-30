import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ref_string', type=str, help='string of integers')
parser.add_argument('--num_frames', type=int, help='integer that defines size of frame.')
args = parser.parse_args()


def check(requests, page_frames):
    index = 0
    faults = 0
    frame = []

    # We will check every item in requests list
    for page in requests:
        # This first conditional is to fill the frame list with the first 3 items, we in
        if page not in frame and len(frame) != page_frames:
            frame.insert(index, page)
            index += 1
            faults += 1
        # Second conditional will remove the item at the index to be removed according to (FIFO), inserts the new
        # item at the new location
        elif page not in frame:
            frame.pop(index)
            frame.insert(index, page)
            index += 1
            faults += 1

        # So we can constraint the list to the size of the number of frames requested we set the index back to 0
        if index == page_frames:
            index = 0

    print(str(faults) + ' faults generated')


if __name__ == '__main__':
    requested = [char for char in args.ref_string]
    check(requested, args.num_frames)
