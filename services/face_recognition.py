import base64

import requests
from PIL import Image

from apps.auth_user.models import Staff
from config import settings


class FaceRecognitionService:
    def __init__(self):
        self.url = settings.FACE_RECOGNITION_URL
        self.intranet_url = settings.INTRANET_URL
        self.min_confidence = 0.75
        self.staff_model = Staff

    def get_user_by_telegram_id(self, telegram_id):
        try:
            return self.staff_model.objects.get(telegram_id=telegram_id)
        except self.staff_model.DoesNotExist:
            return None

    def recognize_face(self, image_data: str):
        url = self.url + "/v1/vision/face/recognize"
        response = requests.post(url,
                                 files={"image": self.base64_to_byte(image_data)},
                                 data={"min_confidence": self.min_confidence}
                                 )
        if response.status_code == 200:
            for item in response.json()["predictions"]:
                item["userid"] = getattr(self.get_user_by_telegram_id(item["userid"]), "full_name", "Unknown")
        return response.json()

    def train_face(self, image_list: list, user_id: str):
        url = self.url + "/v1/vision/face/register"
        files = {}
        for index, image_data in enumerate(image_list, start=1):
            files = {f"image_{index}": self.base64_to_byte(image_data)}
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

    def set_confidence(self, image_data: str, min_confidence: int = 0.67):
        url = self.url + "/v1/vision/face/recognize"
        response = requests.post(
            url,
            files={"image": self.base64_to_byte(image_data)},
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

    def face_detection(self, image_data: str):
        url = self.url + "/v1/vision/face"
        response = requests.post(url, files={"image": self.base64_to_byte(image_data)}).json()
        return response

    def face_detection_and_recognize(self, image_data: str):
        response = self.face_detection(image_data)
        if response.get("predictions", None):
            return self.recognize_face(image_data)
        return response

    def base64_to_byte(self, base64_string: str):
        return base64.b64decode(base64_string)

    def save_image(self, image_data: bytes, image_path: str):
        with open(f"media/faces/{image_path}", "wb") as file:
            file.write(image_data)
        return image_path

    def get_user_data_by_id(self, user_id: str):
        url = self.intranet_url + "/api/staffs/{}/".format(user_id)
        response = requests.get(url).json()
        if response.get("success"):
            return response.get("result")
        return {"full_name": "Unknown"}
