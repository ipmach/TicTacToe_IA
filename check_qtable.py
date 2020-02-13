import numpy as np
from matplotlib import pyplot as plt
import statistics as st
import pprint as pp
from matplotlib.backends.backend_pdf import PdfPages
import datetime

"""
Script use to create a report of a qtable
"""
#path of the q table
path = "agents/QLearningSave/qtable_3x3.npy"


############Script##################
x = np.load(path)

y = np.reshape(x,-1)

stadistics = {"shape":x.shape,"mean": st.mean(y),"high median": st.median_high(y),"variance": st.variance(y)}

pp.pprint(stadistics)
with PdfPages('Reports/qtable_report.pdf') as pdf:
    Tittle = plt.figure(figsize=(6.5,4))
    Tittle.clf()
    Tittle.text(0.5,0.5,"Qtable report", transform=Tittle.transFigure, size=25, ha="center")
    pdf.savefig()
    plt.close()
    a1 = plt.figure(figsize=(6.5,4))
    a1.clf()
    txt = 'In this document we present the q values in an agent file.'
    a1.text(0.38,0.8,"Introduction", transform=a1.transFigure, size=20)
    a1.text(0.14,0.65,"Table path: " + path, transform=a1.transFigure, size=12)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a1.text(0.14,0.59,"Date: " + date, transform=a1.transFigure, size=12)
    a1.text(0.5,0.5,txt, transform=a1.transFigure, size=12, ha="center")
    txt = ' In the graph bellow we can see the qtable.'
    a1.text(0.4,0.4,txt, transform=a1.transFigure, size=12, ha="center")
    pdf.savefig()
    plt.close()
    a2=plt.figure(2)
    a2.suptitle('QTable', fontsize=20)
    plt.imshow(x, aspect='auto')
    pdf.savefig()
    plt.close()
    a2 = plt.figure(figsize=(6.5,4))
    a2.clf()
    a2.text(0.3,0.6,"Stadistics", transform=a1.transFigure, size=20)
    a2.text(0.1,0.5,"Shape: " + str(stadistics["shape"]), transform=a1.transFigure, size=12)
    a2.text(0.1,0.45,"Mean: " + str(stadistics["mean"]), transform=a1.transFigure, size=12)
    a2.text(0.1,0.40,"High median: " + str(stadistics["high median"]), transform=a1.transFigure, size=12)
    a2.text(0.1,0.35,"Variance: " + str(stadistics["variance"]), transform=a1.transFigure, size=12)
    pdf.savefig()
    plt.close()
