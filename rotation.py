from kivy.graphics import *
from kivy.graphics.transformation import Matrix

class SingleRotate(object):
    
    def __init__(self, angle, axis, render_context):
        # It shold be way to get current context
        # but in simple case we may just pass it to constructor 
       self.context = render_context
       self._axis = axis
       self._angle = angle
       self.renderer = render_context
       self.prev_mvm = Matrix()
       self.matrix = Matrix()
       Callback(self._rotate) # here we perform rotation

    def radians(self, degrees):
       """ Calculate radians from angle here """
       return degrees * (3.14159265 / 180.) 

    @property
    def angle(self):
       return self._angle 

    @angle.setter
    def angle(self, v):
       self._angle = v
       angle = self.radians(self._angle)
       ax, ay, az = self._axis
       # calculate rotated matrix and store it
       self.matrix = Matrix().rotate(angle, ax, ay, az)

    def clear(self):
       Callback(self._clear)

    def _rotate(self, *args):
       " This sets rotation in callback "
       # get previous matrix and save it
       self.prev_mvm = self.renderer['modelview_mat']
       # do multiply for rotation
       self.context['modelview_mat'] = self.prev_mvm.multiply(self.matrix)

    def _clear(self, *args):
       self.renderer['modelview_mat'] = self.prev_mvm

