import os

import cv2


def main():
    # this two lines are for loading the videos.
    # in this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
    video_files = [n for n in os.listdir('resource') if n[-4:] == '.flv']
    video_files = sorted(video_files, key=lambda item: int(item.partition('-')[2][:-4]))

    video_index = 0
    cap = cv2.VideoCapture(os.path.join('resource', video_files[video_index]))
    out = cv2.VideoWriter("output.mp4",
                          cv2.VideoWriter_fourcc(*'MP4V'),
                          30, (1280, 720), 1)
    while cap.isOpened():
        ret, frame = cap.read()
        if frame is None:
            print("end of video " + str(video_index) + " .. next one now")
            video_index += 1
            if video_index >= len(video_files):
                break
            cap = cv2.VideoCapture(os.path.join('resource', video_files[video_index]))
            ret, frame = cap.read()
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
