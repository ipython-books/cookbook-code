import os



if __name__ == '__main__':
    filename = '../featured/01_numpy_performance.ipynb'
    
    os.system('ipython nbconvert {f} --to html --template featured.tpl'.format(
        f=filename))
    