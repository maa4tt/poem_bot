import cv2



# make image - fancy playing card using cv2 - not working
def text_card(title, text, indent, filename=r'poem.png'):
    img_path = f'./{filename}'
    image = cv2.imread(img_path)
    image = cv2.resize(image, (1000, 1000))
    org = (175, 220 + indent)
    font = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 0.8
    color = (0, 0, 0)  # (B, G, R)
    thickness = 1
    lineType = cv2.LINE_AA
    bottomLeftOrigin = False
    img_text = cv2.putText(image, text, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin)
    return cv2.imwrite(f'{filename}', img_text)


def title_card(text, filename=r'poem.png'):
    img_path = r'./Blank_Playing_Card.png'
    image = cv2.imread(img_path)
    image = cv2.resize(image, (1000, 1000))
    org = (170, 170)
    font = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 1
    color = (0, 0, 0)  # (B, G, R)
    thickness = 4
    lineType = cv2.LINE_AA
    bottomLeftOrigin = False
    img_text = cv2.putText(image, text, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin)
    print('IMAGE title printed on card')
    return cv2.imwrite(filename, img_text)


def make_card(title, lines, indent=0, filename=r'poem.png'):
    title_card(title, filename)
    for line in lines:
        text_card(title, line, indent, filename)
        indent += 35
    print(f'IMAGE text/title complete card out put to ./{filename}')
    return ()


cv2.waitKey(0)
cv2.destroyAllWindows()
