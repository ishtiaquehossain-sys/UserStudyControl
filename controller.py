import os
from PIL import Image
import shapegenerator
from importlib import reload


class Controller:
    def __init__(self):
        self.generator = None
        self.true_images = None
        self.pred_images = None
        self.summary_images = None

        self.initialize()

    def initialize(self):
        reload(shapegenerator)
        self.generator = shapegenerator.ShapeGenerator()
        self.true_images = {'bench': [], 'table': []}
        self.pred_images = {'bench': [], 'table': []}
        self.summary_images = {}

        for shape in ['bench', 'table']:
            summary_img = Image.new('RGBA', (680, 640))
            for i in range(5):
                for j in range(10):
                    index = str(i) + str(j)
                    true_image = Image.open(os.path.join('shapes', shape, index + '.png')).convert('RGB')
                    pred_image = self.generator.get_image(shape, int(index)).convert('RGB')
                    summary_img.paste(true_image.resize((64, 64)), (i * 138, j * 64))
                    summary_img.paste(pred_image.resize((64, 64)), (64 + i * 138, j * 64))
                    self.true_images[shape].append(true_image)
                    self.pred_images[shape].append(pred_image)
            self.summary_images[shape] = summary_img

    def get_summary(self, shape_name: str):
        return self.summary_images[shape_name]

    def get_details(self, shape_name: str, index: int):
        return self.true_images[shape_name][index], self.pred_images[shape_name][index]
