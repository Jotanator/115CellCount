"""Run the model"""
import glob

import model
import data


def run_training(model_name):
    train_img_files = glob.glob('../data/train/*.jpg')
    print("training images found: ", train_img_files)
    test_img_files = glob.glob('../data/test/*.jpg')

    do_unet = model.DO_UNet(train_img_files,
                            test_img_files,
                            scale_invariant=True)

    do_unet.fit(model_name,
                epochs=10,
                imgs_per_epoch=100,
                batchsize=1,
                workers=8)


    img_files = glob.glob('../data/test/*.jpg')
    do_unet.predict(model_name,
                    img_files,
                    )

def run_prediction(file_dir, model_name):
    train_img_files = glob.glob('../data/train/*.jpg')
    test_img_files = glob.glob('../data/test/*.jpg')
    img_files = glob.glob(f'{file_dir}*.jpg')
    do_unet = model.DO_UNet(train_img_files,
                            test_img_files,
                            scale_invariant=True)
    do_unet.predict(model_name,
                    img_files,
                    )

if __name__ == '__main__':
    run_training('Test_scale')
