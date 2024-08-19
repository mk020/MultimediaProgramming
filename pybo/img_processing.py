import numpy as np
import cv2 as cv

def embossing(img):
    femboss = np.array([[-1.0, 0.0, 0.0],
                        [0.0, 0.0, 0.0],
                        [0.0, 0.0, 1.0]])

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray16 = np.int16(gray)  # gray는 1바이트(8bits) => 16bits
    # int8로 음수를 표현하는 경우 -128~127까지만 표현 가능
    emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))  # 0보다 작으면 0, 255보다 크면 255

    return emboss

def cartoon(img):
    cartoon = cv.stylization(img, sigma_s=60, sigma_r=0.45)
    return cartoon

def pencilGray(img):
    sketch_gray, _ = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_gray

def pencilColor(img):
    _, sketch_color = cv.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    return sketch_color

def oilPainting(img):
    oil = cv.xphoto.oilPainting(img, 10, 1, cv.COLOR_BGR2Lab)  # img: BGR 중 하나 가져옴 / L -> 조명, ab -> 색깔
    return oil

def enhance(img):
    detail = cv.detailEnhance(img, sigma_s=10, sigma_r=0.15)  # s값이 클수록 부드러움, r값이 클수록 엣지 강화
    return detail