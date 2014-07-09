########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Tuesday 17 April 2007 10:12:45 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/MergeText_net.py,v 1.2 2007/08/29 20:37:16 vareille Exp $
#
# $Id: MergeText_net.py,v 1.2 2007/08/29 20:37:16 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

try:
    ## saving node RandNormDist ##
    from Vision.matplotlibNodes import RandNormDist
    RandNormDist_14 = RandNormDist(constrkw = {}, name='RandNormDist', library=matplotliblib)
    masterNet.addNode(RandNormDist_14,70,37)
    apply(RandNormDist_14.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore RandNormDist named RandNormDist in network masterNet"
    print_exc()
    RandNormDist_14=None

try:
    ## saving node Histogram ##
    from Vision.matplotlibNodes import HistogramNE
    Histogram_15 = HistogramNE(constrkw = {}, name='Histogram', library=matplotliblib)
    masterNet.addNode(Histogram_15,84,436)
    apply(Histogram_15.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore HistogramNE named Histogram in network masterNet"
    print_exc()
    Histogram_15=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_16 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_16,128,188)
    Text_16.inputPortByName['posx'].widget.set(0.583333333333, run=False)
    Text_16.inputPortByName['posy'].widget.set(0.902777777778, run=False)
    Text_16.inputPortByName['textlabel'].widget.set("BAR MIDDLE", run=False)
    apply(Text_16.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_16=None

try:
    ## saving node MergeText ##
    from Vision.matplotlibNodes import MPLMergeTextNE
    MergeText_17 = MPLMergeTextNE(constrkw = {}, name='MergeText', library=matplotliblib)
    masterNet.addNode(MergeText_17,385,378)
except:
    print "WARNING: failed to restore MPLMergeTextNE named MergeText in network masterNet"
    print_exc()
    MergeText_17=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_18 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_18,294,33)
    Text_18.inputPortByName['posx'].widget.set(0.419444444444, run=False)
    Text_18.inputPortByName['posy'].widget.set(0.65, run=False)
    Text_18.inputPortByName['textlabel'].widget.set("BAR LEFT", run=False)
    Text_18.inputPortByName['rotation'].widget.set(90.0, run=False)
    Text_18.inputPortByName['verticalalignment'].widget.set("top", run=False)
    apply(Text_18.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_18=None

try:
    ## saving node Text ##
    from Vision.matplotlibNodes import Text
    Text_19 = Text(constrkw = {}, name='Text', library=matplotliblib)
    masterNet.addNode(Text_19,455,192)
    Text_19.inputPortByName['posx'].widget.set(0.294444444444, run=False)
    Text_19.inputPortByName['posy'].widget.set(0.127777777778, run=False)
    Text_19.inputPortByName['textlabel'].widget.set("BAR END", run=False)
    Text_19.inputPortByName['rotation'].widget.set(45.0, run=False)
    apply(Text_19.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Text named Text in network masterNet"
    print_exc()
    Text_19=None

masterNet.freeze()

## saving connections for network RandomNormDist ##
if RandNormDist_14 is not None and Histogram_15 is not None:
    try:
        masterNet.connectNodes(
            RandNormDist_14, Histogram_15, "data", "values", blocking=True)
    except:
        print "WARNING: failed to restore connection between RandNormDist_14 and Histogram_15 in network masterNet"
if Text_16 is not None and MergeText_17 is not None:
    try:
        masterNet.connectNodes(
            Text_16, MergeText_17, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_16 and MergeText_17 in network masterNet"
if MergeText_17 is not None and Histogram_15 is not None:
    try:
        masterNet.connectNodes(
            MergeText_17, Histogram_15, "drawAreaDef", "drawAreaDef", blocking=True)
    except:
        print "WARNING: failed to restore connection between MergeText_17 and Histogram_15 in network masterNet"
if Text_18 is not None and MergeText_17 is not None:
    try:
        masterNet.connectNodes(
            Text_18, MergeText_17, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_18 and MergeText_17 in network masterNet"
if Text_19 is not None and MergeText_17 is not None:
    try:
        masterNet.connectNodes(
            Text_19, MergeText_17, "drawAreaDef", "textlist", blocking=True)
    except:
        print "WARNING: failed to restore connection between Text_19 and MergeText_17 in network masterNet"
masterNet.unfreeze()
#masterNet.run()
