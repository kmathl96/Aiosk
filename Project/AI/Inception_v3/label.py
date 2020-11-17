import tensorflow.compat.v1 as tf, sys
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import numpy as np
import time
from PIL import Image
import os, cv2, glob, dlib
import matplotlib.pyplot as plt

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

# # change this as you see fit
# imagepath = sys.argv[1]
imagePath = './tmp/10.jpg'                                      # 추론을 진행할 이미지 경로
modelFullPath = './tmp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = './tmp/output_labels.txt'                                   # 읽어들일 labels 파일 경로



def change_grayscale(path, x1, y1, x2, y2):
# def change_grayscale(path):
    temp = Image.open(path)
    # temp = cv2.imread(path)
    # plt.imshow(temp)
    temp_numpy = np.array(temp, 'uint8')
    temp_numpy = temp_numpy[y1:y2, x1:x2]
    try:
        gray = cv2.cvtColor(temp_numpy, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path, gray)
        # convert image visualization
        # plt.imshow(gray)
        # plt.show()
    except:
        pass

def face_detector(path):
    img = cv2.imread(path)

    detector = dlib.get_frontal_face_detector()

    faces = detector(img)
    x1, y1 = 0, 0
    y2, x2 = img.shape[:2]
    for face in faces:
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
    return x1, y1, x2, y2


def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image():
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        print(answer)
        return answer


if __name__ == '__main__':
    starttime = time.time()
    x1,y1,x2,y2 = face_detector(imagePath)
    print(x1,y1,x2,y2)
    change_grayscale(imagePath, x1, y1, x2, y2)
    # change_grayscale(imagePath)
    run_inference_on_image()
    print("elapsed time : ", round(time.time()-starttime, 2) ,'sec')

