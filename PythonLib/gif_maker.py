import imageio


def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, "GIF", duration=1)

    return


if __name__ == "__main__":
    image_list = ["Snip20190424_31.png", "Snip20190424_33.png"]
    gif_name = "created_gif.gif"
    create_gif(image_list, gif_name)
