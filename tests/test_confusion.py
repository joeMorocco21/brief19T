from argparse import Namespace
import torch
import pytest
from App.apps import classNames as classy, model
from App.app import *
from App.mednet import MedNet


class Testy_class():
    def test_shape(self):
        #dataset = model()
        assert(len(classy) == 6)
        #sample, _ = dataset.train_data[0]
    #assert model(inputs).shape == torch.Size([len(inputs), numC])
        #self.assertEqual(torch.Shape((6, 64, 64)), sample.shape)