"""

    script generateGifs.py

    This script generates multiple animated gif cross-sections of data
    from the MITgcm model.

    For each animation set parameters

    'cut_var':      Which coordinate cross section (one of 'x', 'y', 'z')
    'cut_val':      Value at which to cross section (in meters)
    'data_var':     Variable prefix in the .data and .meta files
    'movie_name':   Filename of the generated movie (without extension)

    Call the plot(gif_args) function with a dictionary containing these args.

    Optional parameters:

    # vmin and vmax: Desired min and max for the colourbar scale. If not given, scale will likely be inconsistent. Not required for temperature
    # file_type: The file type to save the images in. By default, saves as a png. Options are 'emf', 'eps', 'pdf', 'png', 'ps', 'raw', 'rgba', 'svg', and 'svgz'
    # stitch_gif: Boolean controlling whether or not to stitch the images into a gif. By defualt, True
    # iter_start, iter_end: the range of iterations to plot, inclusive. By default, the entire runtime is plotted
    # x_axis_start, x_axis_end: the range of the x-axis coordinate to plot, in meters and inclusive. By default, entire range is plotted
    # y_axis_start, y_axis_end: the range of the y-axis coordinate to plot, in meters and inclusive. By default, entire range is plotted
    # image_folder_name: name of the folder to save images in. By defualt, "PNG_IMAGES"
    # gif_folder_name: name of the folder to save gifs in. By default, "GIF_MOVIES"
    # bathy_file_name: name of the bathymetry file used as input. By default, "bathymetry.bin"

    # TODO finish this list of optional parameters

"""

from twodimensionalgif import twodimensionalgif

def plot(gif_args):
    d = global_gif_args.copy()
    d.update(gif_args)
    twodimensionalgif(d)

global_gif_args = {

}

#####

gif_args = {
    'cut_var' : 'z',
    'cut_val' : 0,
    'data_var' : 'T',
    'movie_name' : 'T_0_xy_interp'
}
plot(gif_args)


gif_args = {
    'cut_var' : 'x',
    'cut_val' : 4825,
    'data_var' : 'T',
    'movie_name' : 'T_4825_zy_interp'
}
plot(gif_args)

gif_args = {
    'cut_var' : 'y',
    'cut_val' : 975,
    'data_var' : 'T',
    'movie_name' : 'T_975_zx_interp'
}
plot(gif_args)

#gif_args = {
#    'cut_var' : 'z',
#    'cut_val' : 0,
#    'data_var' : 'V',
#    'movie_name' : 'V_0_xy'
#}
#plot(gif_args)

print ("\nFinished animating all the gifs")
