import argparse
import queue

parser = argparse.ArgumentParser()
parser.add_argument('--ref_string', type=str, help='string of integers')
parser.add_argument('--num_frames', type=int, help='integer that defines size of frame.')
args = parser.parse_args()


def check(requests, page_frames):
    i = 0
    j = 0
    frame = []

    for page in requests:
        if page not in frame and len(frame) != 3:
            frame.insert(i, page)
            i += 1
            j += 1
        elif page not in frame:
            frame.pop(i)
            frame.insert(i, page)
            j += 1
            i += 1

        if i == page_frames:
            i = 0

    print(str(j) + ' faults generated')


if __name__ == '__main__':
    requested = [char for char in args.ref_string]
    check(requested, args.num_frames)
