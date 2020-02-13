import numpy as np
from matplotlib import pyplot as plt
import statistics as st
import pprint as pp
import datetime
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, NoEscape, TextBlock,Center
from pylatex.utils import italic,bold

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

doc = Document('basic')
doc.preamble.append(Command('title', 'Qtable report'))
doc.preamble.append(Command('author', 'Tic Tac Toe'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

with doc.create(Section('Introducction')):
        doc.append(bold('This document was autogenerate. '))
        doc.append('Here we present the saved q values of an agent (path: ')
        doc.append(italic(path))
        doc.append('). This document present a image with the respective values of the elements on the qtable.' \
        + 'and the stadistics values obtain in the process. ')
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        doc.append(bold('Document generate ' + date  + '.'))

with doc.create(Section('Qtable')):
    doc.append('In this secction we can see the image of the qtable, each color represent a different value.')
    with doc.create(Figure(position='htbp')) as plot:
            a2=plt.figure(2)
            a2.suptitle('QTable', fontsize=20)
            plt.imshow(x, aspect='auto')
            plt.colorbar()
            plot.add_plot()
            plot.add_caption('Image of the qtable.')

with doc.create(Section('Stadistics')):
    doc.append('Here we can see some basice stadistics token from the qtable of the agent.')
    with doc.create(Center()) as centered:
        with centered.create(Tabular('|r|l|')) as table:
            table.add_hline()
            table.add_row(("Shape", stadistics["shape"]))
            table.add_hline()
            table.add_row(("Mean", stadistics["mean"]))
            table.add_hline()
            table.add_row(("High median", stadistics["high median"]))
            table.add_hline()
            table.add_row(("Variance", stadistics["variance"]))
            table.add_hline()


doc.generate_pdf('Reports/qtable_report', clean_tex=True)
