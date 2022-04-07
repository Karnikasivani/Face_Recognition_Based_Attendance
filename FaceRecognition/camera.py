from scipy.spatial.distance import cosine
import mtcnn
from keras.models import load_model
from utils import *



class VideoCamera(object):

            def __init__(self):
                self.video = cv2.VideoCapture(0)

            def __del__(self):
                self.video.release()
            def get_frame(self):
                global encode, distance, name, pt_1, pt_2, jpeg
                success, image = self.video.read()
                encoder_model = 'facenet_keras.h5'
                encodings_path = 'data/encodings/encodings.clf'

                detector = mtcnn.MTCNN()
                encoder = load_model(encoder_model)
                encoding_dict = load_pickle(encodings_path)
                recognition_t = 0.68
                confidence_t = 0.99
                required_size = (160, 160)

                img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                while True:
                    results = detector.detect_faces(img_rgb)
                    for res in results:
                        if res['confidence'] < confidence_t:
                            continue
                        face, pt_1, pt_2 = get_face(img_rgb, res['box'])
                        encode = get_encode(encoder, face, required_size)
                        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
                        name = 'unknown'
                        distance = float("inf")
                        for db_name, db_encode in encoding_dict.items():
                            dist = cosine(db_encode, encode)
                            if dist < recognition_t and dist < distance:
                                name = db_name
                                distance = dist
                        if name == 'unknown':
                            cv2.rectangle(image, pt_1, pt_2, (0, 0, 255), 2)
                            cv2.putText(image, name, pt_1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
                        else:
                            cv2.rectangle(image, pt_1, pt_2, (0, 255, 0), 2)
                            cv2.putText(image, name + f'__{distance:.2f}', (pt_1[0], pt_1[1] - 5),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 200, 200), 2)


                        ret, jpeg = cv2.imencode('.jpg', image)
                        data = []
                        data.append(jpeg.tobytes())
                        data.append(name)
                        return data

