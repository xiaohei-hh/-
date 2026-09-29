import cv2
import matplotlib.pyplot as plt

def flip_image(image_path):
    # 读取图片
    img = cv2.imread(image_path)
    if img is None:
        print("图片读取失败，请检查路径")
        return

    # 左右翻转
    flipped = cv2.flip(img, 1)

    # 显示翻转图和原图（位置已对调）
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)      # 左边：翻转图
    plt.title("Flipped")
    plt.imshow(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 2, 2)      # 右边：原图
    plt.title("Original")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.show()

    return flipped

if __name__ == "__main__":
    flip_image("test.jpg")