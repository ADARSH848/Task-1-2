import cv2

cap = cv2.VideoCapture('input_video.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (int(cap.get(3)), int(cap.get(4))), isColor=True)

count = 0
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    count += 1

    if count % 4 == 0:
        out.write(frame)

    cv2.imshow('Output Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
