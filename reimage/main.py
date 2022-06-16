from PIL import Image
import cv2

def main():
    cap = cv2.VideoCapture(0)

    while (cap.isOpened()):
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imwrite("input.png", frame)
        trigger_rgb("input.png", 38, 128, 178, 40)

        cv2.imshow("Input", frame)
        cv2.imshow('Output', cv2.imread('output.png'))
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()


def trigger_rgb(file, r_req, g_req, b_req, marge):
    image = file
    image = Image.open(image)
    pix = image.load()
    xsize, ysize = image.size
    for x in range(xsize):
        for y in range(ysize):
            r, g, b = pix[x, y]
            if r_req + marge >= r >= r_req - marge and g_req + marge >= g >= g_req - marge and b <= b_req + marge and b_req >= b_req - marge:
                pix[x, y] = (255, 255, 0)
    image.save('output.png')
    return image


if __name__ == '__main__':
    main()
