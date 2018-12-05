#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
'''
Single switch connected to n hosts.
'''
class SingleSwitchTopo(Topo):
    def build(self):
        #add switch
<<<<<<< HEAD
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		#add host
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
        #add link
		self.addLink(h1, s1, bw = 12, delay = '6ms', loss = 2)
		self.addLink(s1, s8, bw = 20, delay = '7ms', loss = 15)
		self.addLink(s8, s6, bw = 30, delay = '1ms', loss = 12)
		self.addLink(s6, h2, bw = 18, delay = '2ms', loss = 3)
		self.addLink(s8, s4, bw = 23, delay = '6ms', loss = 10)
		self.addLink(s4, h5, bw = 14, delay = '5ms', loss = 2)
		self.addLink(s8, s2, bw = 25, delay = '6ms', loss = 14)
		self.addLink(s2, s9, bw = 30, delay = '3ms', loss = 18)
		self.addLink(s9, s7, bw = 33, delay = '8ms', loss = 10)
		self.addLink(s3, s9, bw = 35, delay = '2ms', loss = 17)
		self.addLink(s7, h3, bw = 18, delay = '6ms', loss = 6)
		self.addLink(s5, h6, bw = 15, delay = '4ms', loss = 3)
		self.addLink(s9, s5, bw = 30, delay = '3ms', loss = 20)
		self.addLink(h4, s3, bw = 13, delay = '3ms', loss = 5)
=======
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        #add host
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        #add link
            self.addLink(h1, s1, bw = 12, delay = '6ms', loss = 2%)
            self.addLink(s1, s8, bw = 20, delay = '7ms', loss = 15%)
            self.addLink(s8, s6, bw = 30, delay = '1ms', loss = 12%)
            self.addLink(s6, h2, bw = 18, delay = '2ms', loss = 3%)
            self.addLink(s8, s4, bw = 23, delay = '6ms', loss = 10%)
            self.addLink(s4, h5, bw = 14, delay = '5ms', loss = 2%)
            self.addLink(s8, s2, bw = 25, delay = '6ms', loss = 14%)
            self.addLink(s2, s9, bw = 30, delay = '3ms', loss = 18%)
            self.addLink(s9, s7, bw = 33, delay = '8ms', loss = 10%)
            self.addLink(s3, s9, bw = 35, delay = '2ms', loss = 17%)
            self.addLink(s7, h3, bw = 18, delay = '6ms', loss = 6%)
            self.addLink(s5, h6, bw = 15, delay = '4ms', loss = 3%)
            self.addLink(s9, s5, bw = 30, delay = '3ms', loss = 20%)
            self.addLink(h4, s3, bw = 13, delay = '3ms', loss = 5%)
>>>>>>> a3a3a55a7c773836e6f74e59e95d96fcc9e34415

'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 6 hosts and 9 switch
    topo = SingleSwitchTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    # Dump every host and switches connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    # Add the following code and do NOT use net.stop()
    CLI(net)
'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
