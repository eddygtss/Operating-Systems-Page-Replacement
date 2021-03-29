import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ref_string', type=str, help='string of integers')
parser.add_argument('--num_frames', type=int, help='integer that defines size of memory to allocate.')
args = parser.parse_args()


def check(requests, frames):
    print(requests)

    i = 0
    j = 0
    loop = 0
    frame = []

    for char in requests:
        if len(frame) < frames:
            frame.append(char)
            j += 1

        if char != frame[i]:
            frame.pop(i)
            frame.insert(i, char)
            j += 1
        print(frame)

        if i == 2:
            i = 0
        else:
            i += 1
        loop += 1
    print(j)
    print(loop)


if __name__ == '__main__':
    requested = [char for char in args.ref_string]
    check(requested, args.num_frames)
