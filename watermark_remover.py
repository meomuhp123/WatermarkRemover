import os
import sys
import cv2
import numpy as np
from moviepy import editor
import PySimpleGUI as sg
from pyngrok import ngrok

VIDEO_PATH = 'video'
OUTPUT_PATH = 'output'
TEMP_VIDEO = 'temp.mp4'

class WatermarkRemoverGUI:
    def __init__(self):
        self.window = None

    def create_window(self):
        layout = [
            [sg.Text('Threshold:'), sg.InputText(default_text='80', key='-THRESHOLD-')],
            [sg.Text('Kernel Size:'), sg.InputText(default_text='5', key='-KERNEL_SIZE-')],
            [sg.Button('Remove Watermark'), sg.Button('Remove Subtitle')]
        ]

        self.window = sg.Window('Watermark Remover', layout)

    def select_roi(self, img: np.ndarray, hint: str) -> list:
        '''
        Code để chọn ROI tại đây
        '''

    def remove_watermark(self, threshold: int, kernel_size: int):
        remover = WatermarkRemover(threshold=threshold, kernel_size=kernel_size)
        remover.remove_video_watermark()

    def remove_subtitle(self, threshold: int, kernel_size: int):
        remover = WatermarkRemover(threshold=threshold, kernel_size=kernel_size)
        remover.remove_video_subtitle()

    def run(self):
        self.create_window()

        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Remove Watermark':
                threshold = int(values['-THRESHOLD-'])
                kernel_size = int(values['-KERNEL_SIZE-'])
                self.remove_watermark(threshold, kernel_size)

            if event == 'Remove Subtitle':
                threshold = int(values['-THRESHOLD-'])
                kernel_size = int(values['-KERNEL_SIZE-'])
                self.remove_subtitle(threshold, kernel_size)

        self.window.close()

if __name__ == '__main__':
    remover_gui = WatermarkRemoverGUI()
    remover_gui.run()

    # Khởi tạo localhost bằng pyngrok
    public_url = ngrok.connect(port='80')
    print(f"URL của giao diện GUI: {public_url}")

    # Đóng kết nối localhost
    ngrok.disconnect(public_url)