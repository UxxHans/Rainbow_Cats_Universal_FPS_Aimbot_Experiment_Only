import cv2
import mediapipe as mp


class PoseDetector:

    def __init__(self,
                 static_image_mode=False,
                 model_complexity=False,
                 smooth_landmarks=True,
                 enable_segmentation=True,
                 smooth_segmentation=True,
                 min_detection_confidence=0.6,
                 min_tracking_confidence=0.9
                 ):

        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.enable_segmentation = enable_segmentation
        self.smooth_segmentation = smooth_segmentation
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.static_image_mode,
                                     self.model_complexity,
                                     self.smooth_landmarks,
                                     self.enable_segmentation,
                                     self.smooth_segmentation,
                                     self.min_detection_confidence,
                                     self.min_tracking_confidence)

    def find_position(self, image):
        self.results = self.pose.process(cv2.cvtColor(image, cv2.COLOR_RGBA2RGB))

        track_points_list = []
        if self.results.pose_landmarks:
            for i in range(0, 33):
                x = self.results.pose_landmarks.landmark[i].x
                y = self.results.pose_landmarks.landmark[i].y
                h, w, c = image.shape
                cx, cy = x * w, y * h
                track_points_list.append([cx, cy])

        return track_points_list
