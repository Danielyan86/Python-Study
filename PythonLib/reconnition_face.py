from PIL import Image
import face_recognition


def get_face_images(picture_path):
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file(picture_path)

    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print(
            "A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom,
                                                                                                  right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        print(picture_path)
        pil_image.save("{0}.jpg".format(picture_path[-7:-3]))


if __name__ == '__main__':
    import os

    pic_path = "/Users/xyan/pycharm_project/Movie-scrapy/movie/images/full"
    pic_path_format = "/Users/xyan/pycharm_project/Movie-scrapy/movie/images/full/{0}"
    res = os.listdir(pic_path)
    for pic in res:
        print(pic)
        get_face_images(pic_path_format.format(pic))
