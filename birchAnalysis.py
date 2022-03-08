import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import Birch
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
import esData

# Source: https://stackoverflow.com/questions/45729092/make-interactive-matplotlib-window-not-pop-to-front-on-each-update-windows-7
# Wird benötigt, da sonst die Abbilding bei jedem Update in den Vordergrund rückt
def mypause(interval):
    backend = plt.rcParams['backend']
    if backend in plt.rcsetup.interactive_bk:
        figManager = plt._pylab_helpers.Gcf.get_active()
        if figManager is not None:
            canvas = figManager.canvas
            if canvas.figure.stale:
                canvas.draw()
            canvas.start_event_loop(interval)
            return

# Ignoriere Warnungen, dass nur ein Cluster vorhanden ist
@ignore_warnings(category=ConvergenceWarning)
def drawPlot():
    dataList = esData.elasticRequest()
    X = np.array(dataList)
    model = Birch(branching_factor=70,n_clusters=2, threshold=4.5).fit(X)
    pred = model.predict(X)
    clusters = np.unique(model.labels_).size
    plt.scatter(X[:,0], X[:,1], c=pred)
    if (clusters == 2):
        plt.title(f"Anzahl an Cluster: {clusters}\nAnomalie erkannt!")
    else:
        plt.title(f"Anzahl an Cluster: {clusters}")
    plt.xlabel('Vergangene Zeit in Minuten')
    plt.ylabel('Speicherauslastung in %')

fig = plt.figure()
fig.show()
while True:
    drawPlot()
    mypause(15)
    plt.clf()
