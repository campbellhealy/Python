# matplotlib tutorial - lifecycle
'''
     I rewrote this tutorial as it didn't make sense to me on the first reading.
     What should/should not be included for each section of the tutorial.
     It is split into two parts, the second part is using additional functionality # 7
     Adjust the __name__ to allow for use of each part.
'''
import numpy as np
import matplotlib.pyplot as plt
from os import system


data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)


def tutorial_part_one():
    system('cls')
    # 1
    #  first generate an instance of figure.Figure and axes.Axes
    # fig, ax = plt.subplots()

    # 2
    # To see a list of styles, we can use style
    print(plt.style.available)
    # Convert available styles into a list to use
    styles = list(plt.style.available)
    print(styles[8])
    #  Activate a style with
    plt.style.use(styles[8])
  
    # 3
    # Plot on top of of the blank above
    # fig, ax = plt.subplots()
    # ax.barh(group_names, group_data)

    # 4
    # Tune the look of the plot

    # 4a
    # Rotate the labels
    # fig, ax = plt.subplots()
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()

    # 4b
    # Change multiple properties with pyplot.setp()
    # fig, ax = plt.subplots()
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')

    # 4c 
    # In 4b the x labels were cut off, to auto make room for the labels set the autolayout value in rcParams
    # From this point the next line should not be remarked out
    plt.rcParams.update({'figure.autolayout': True})

    # fig, ax = plt.subplots()
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')

    # 5
    # Label the plot usinf Artist.set() method to set properties of the Axes object
    # fig, ax = plt.subplots()
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')
    # ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
    #     title='Company Revenue')
    
    # 6 
    # Adjust plot size with pyplot.subplots() keyword argument figsize(width, height)
    # fig, ax = plt.subplots(figsize=(8, 4))
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')
    # ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
    #     title='Company Revenue')

    # Use this to render the plot to the screen
    plt.show()
    # tutorial_part_one ends here

    
# 7 
# Customise labels with a function that takes an int and returns a str

def currency(x, pos):
    """The two arguments are the value and tick position"""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

def  tutorial_part_two():
    system('cls')
    # Bring this forward from the tutorial_part_one
    plt.rcParams.update({'figure.autolayout': True})

    # 8
    # Apply the currency fuction to the labels
    # fig, ax = plt.subplots(figsize=(6, 8))
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')

    # ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
    #     title='Company Revenue')   
    # ax.xaxis.set_major_formatter(currency)

    # 9
    # draw multiple plot elements on the same instance of axes.Axes by calling another plot method on the object

    # fig, ax = plt.subplots(figsize=(8, 8))
    # ax.barh(group_names, group_data)
    # labels = ax.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')

    # # Add a vertical line, here we set the style in the function call
    # ax.axvline(group_mean, ls='--', color='r')

    # # Annotate new companies
    # for group in [3, 5, 8]:
    #     ax.text(145000, group, "New Company", fontsize=10,
    #             verticalalignment="center")

    # # Now we move our title up since it's getting a little cramped
    # ax.title.set(y=1.05)
    # ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
    #     title='Company Revenue')

    # ax.xaxis.set_major_formatter(currency)
    # ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
    # # fig.subplots_adjust(right=.1)  #  remarke out as ValueError: left cannot be >= right

    # 10
    # File format options 
    # print(fig.canvas.get_supported_filetypes())

    # 11
    # Use figure.Figure.savefig() to save to disk.
    '''
         Useful flags:
            - transparent=True makes the background of the saved figure transparent if the format supports it.
            - dpi=80 controls the resolution (dots per square inch) of the output.
            - bbox_inches="tight" fits the bounds of the figure to our plot
    '''
    # fig.savefig('sales.pdf', transparent=False, dpi=80, bbox_inches="tight")
    # fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
    # fig.savefig('sales.ps', transparent=False, dpi=80, bbox_inches="tight")

    # Use this to render the plot to the screen
    plt.show()




if __name__ == '__main__':
    # tutorial_part_one()
    tutorial_part_two()