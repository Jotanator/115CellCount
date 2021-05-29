"""Run the model"""
import glob
import numpy as np
import model
import data
from PIL import Image
import json


def run_training(model_name):
    train_img_files = glob.glob('../data/train/*.jpg')
    #print("training images found: ", train_img_files)
    test_img_files = glob.glob('../data/test/*.jpg')

    do_unet = model.DO_UNet(train_img_files,
                            test_img_files,
                            scale_invariant=True)

    fitted_model = do_unet.fit(model_name,
                epochs=10,
                imgs_per_epoch=1000,
                batchsize=8,
                workers=1)

    # Serializing json 
    json_object = json.dumps(fitted_model.history, indent = 18)
  
    # Writing to sample.json
    with open("Output_training.json", "w") as outfile:
      outfile.write(json_object)

    print('printing summary')
    do_unet.model.summary()
    print('printed summary')

    img_files = glob.glob('../data/test/*.jpg')
    print("Result:")
    array = do_unet.predict(model_name,
                    img_files,
                    )
    print(array)
    np.save("../data/test/380", array)
    img = Image.fromarray(array[1][0], 'RGB')
    img.save('../data/test/new.png')
    img.show()

def run_prediction(file_dir, model_name):
    train_img_files = glob.glob('../data/train/*.jpg')
    test_img_files = glob.glob('../data/test/*.jpg')
    img_files = glob.glob(f'{file_dir}*.jpg')
    do_unet = model.DO_UNet(train_img_files,
                            test_img_files,
                            scale_invariant=True)
    do_unet.model.load_weights('models/Test_scale_best.h5')
    do_unet.predict(model_name,
                    img_files,
                    )

if __name__ == '__main__':
    run_training('Test_scale')