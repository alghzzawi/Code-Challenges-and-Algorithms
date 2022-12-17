# Write your test here
from challenge01 import Grahp
import pytest

def test_BFS_1():
    grahp1 = Grahp()

    a = grahp1.add_node('A')
    b = grahp1.add_node('B')
    c = grahp1.add_node('C')
    d = grahp1.add_node('D')
    e = grahp1.add_node('E')
    f = grahp1.add_node('F')
    g = grahp1.add_node('G')
    h = grahp1.add_node('H')
    i = grahp1.add_node('I')
    k = grahp1.add_node('K')

    grahp1.add_edge(a,b)
    grahp1.add_edge(a,e)
    grahp1.add_edge(a,c)
    grahp1.add_edge(b,d)
    grahp1.add_edge(e,g)
    grahp1.add_edge(e,d)
    grahp1.add_edge(e,f)
    grahp1.add_edge(g,h)
    grahp1.add_edge(f,h)
    grahp1.add_edge(f,i)
    grahp1.add_edge(h,k)
    grahp1.add_edge(i,k)

    
    actual = grahp1.BFS(a)
    extcepted = ['A', 'B', 'E', 'C', 'D', 'G', 'F', 'H', 'I', 'K']
    assert actual == extcepted