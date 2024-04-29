import requests
from PIL import Image


class FaceRecognitionService:
    def __init__(self):
        self.url = "http://127.0.0.1:8080"
        # self.url = "http://80.80.212.224:60033"

    def recognize_face(self, image_data: bytes):
        url = self.url + "/v1/vision/face/recognize"
        # image_data = open(image_path, "rb").read()
        response = requests.post(url, files={"image": image_data}).json()
        return response

    def train_face(self, image_list: list, user_id: str):
        url = self.url + "/v1/vision/face/register"
        files = {}
        for index, image_path in enumerate(image_list, start=1):
            files = {f"image_{index}": image_path}
        response = requests.post(url, files=files, data={"userid": user_id}).json()
        return response

    def delete_face(self, user_id):
        url = self.url + "/v1/vision/face/delete"
        response = requests.post(url, data={"userid": user_id}).json()
        return response

    def face_list(self):
        url = self.url + "/v1/vision/face/list"
        faces = requests.post(url).json()
        return faces

    def set_confidence(self, image_data, min_confidence: int = 0.67):
        url = self.url + "/v1/vision/face/recognize"
        response = requests.post(
            url,
            files={"image": image_data},
            data={"min_confidence": min_confidence},
        ).json()
        return response

    def show_face(self, image_data, min_confidence: int = 0.67):
        url = self.url + "/v1/vision/face/recognize"
        image_data = open(self.image_path, "rb").read()
        image = Image.open(self.image_path).convert("RGB")
        response = requests.post(
            url,
            files={"image": image_data},
            data={"min_confidence": min_confidence},
        ).json()

        for face in response["predictions"]:
            userid = face["userid"]
            y_max = int(face["y_max"])
            y_min = int(face["y_min"])
            x_max = int(face["x_max"])
            x_min = int(face["x_min"])
            cropped = image.crop((x_min, y_min, x_max, y_max))
            cropped.save("{}.jpg".format(userid))

        return response
