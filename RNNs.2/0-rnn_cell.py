import numpy as np 

class RNNCell:
  """Create RNN class"""
  def __init__(self, i, h, o):
      """
      i: dimensionality of the data
      h: dimensionality of the hidden state
      o: dimensionality of the outputs

      Wh, bh, Wy, by: weights and biases.
      """
      self.Wh = np.random.randn(i+h, h)
      self.bh = np.zeros((1,h))
      self.Wy = np.random.randn(h,o)
      self.by = np.zeros(1,o)

  def forward(self, h_prev, x_t):
    """
    Performs forward propagation for one time step
    """
   concat = np.concatenate((h_prev, _t), axis=1)
