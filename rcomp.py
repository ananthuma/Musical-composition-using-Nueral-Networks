from pybrain.structure import RecurrentNetwork
n = RecurrentNetwork()
n.addInputModule(LinearLayer(14, name='in'))
n.addModule(SigmoidLayer(100, name='hidden'))
n.addOutputModule(LinearLayer(90, name='out'))
n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))
n.addRecurrentConnection(FullConnection(n['hidden'], n['hidden'], name='c3'))