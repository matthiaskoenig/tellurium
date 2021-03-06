# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:31:51 2014

@author: mgaldzic
"""

import tellurium as te
# Setting boundary species in a model
model = '''
  model cell()
    # The $ character is used to indicate that a particular species is FIXED
    $S1 -> S2; k1*S1
     S2 -> S3; k2*S2 - k3*S3
     S3 -> $S4; Vm*S3/(Km + S3)

    # Initialize values
    S1 = 1.0; S2 = 0; S3 = 0; S4 = 0.0
    k1 = 0.2; k2 = 0.67; k3 = 0.04
    Vm = 5.6; Km = 0.5
  end
'''

r = te.loadAntimonyModel(model)
result = r.simulate (0, 50, 200)
te.plotWithLegend (r, result)
