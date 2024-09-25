from __future__ import annotations
from abc import ABC, abstractmethod
from layer_util import Layer
import layers

class LayerStore(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store.
        Returns true if the LayerStore was actually changed.
        """
        pass

    @abstractmethod
    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.
        """
        pass

    @abstractmethod
    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer
        Returns true if the LayerStore was actually changed.
        """
        pass

    @abstractmethod
    def special(self):
        """
        Special mode. Different for each store implementation.
        """
        pass

class SetLayerStore(LayerStore):
    """
    Set layer store. A single layer can be stored at a time (or nothing at all)
    - add: Set the single layer.
    - erase: Remove the single layer. Ignore what is currently selected.
    - special: Invert the colour output.
    """
    def __init__(self) -> None:
        self.mylayer = None
        self.invert = False 

    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store.
        Returns true if the LayerStore was actually changed.
        """
        if (self.mylayer == Layer):
            return False 
        else :
            self.mylayer = Layer 
            return True

    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.
        """
        if (self.invert == True) :
            color_get = layers.invert.apply(start,timestamp,x,y)
        else :
            if (self.mylayer == None):
                color_get = start 
            else:
                color_get = Layer.apply(start,timestamp,x,y)
        return color_get
            

    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer
        Returns true if the LayerStore was actually changed.
        """
        if (self.mylayer == None):
            return False 
        else :
            self.mylayer = None
            return True

    def special(self):
        """
        Special mode. Different for each store implementation.
        """
        self.invert = not(self.invert)

class AdditiveLayerStore(LayerStore):
    """
    Additive layer store. Each added layer applies after all previous ones.
    - add: Add a new layer to be added last.
    - erase: Remove the first layer that was added. Ignore what is currently selected.
    - special: Reverse the order of current layers (first becomes last, etc.)
    """
    def __init__(self) -> None:
        pass

    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store.
        Returns true if the LayerStore was actually changed.
        """
        pass

    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.
        """
        pass

    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer
        Returns true if the LayerStore was actually changed.
        """
        pass

    def special(self):
        """
        Special mode. Different for each store implementation.
        """
        pass
    pass

class SequenceLayerStore(LayerStore):
    """
    Sequential layer store. Each layer type is either applied / not applied, and is applied in order of index.
    - add: Ensure this layer type is applied.
    - erase: Ensure this layer type is not applied.
    - special:
        Of all currently applied layers, remove the one with median `name`.
        In the event of two layers being the median names, pick the lexicographically smaller one.
    """
    def __init__(self) -> None:
        pass

    def add(self, layer: Layer) -> bool:
        """
        Add a layer to the store.
        Returns true if the LayerStore was actually changed.
        """
        pass

    def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
        """
        Returns the colour this square should show, given the current layers.
        """
        pass

    def erase(self, layer: Layer) -> bool:
        """
        Complete the erase action with this layer
        Returns true if the LayerStore was actually changed.
        """
        pass

    def special(self):
        """
        Special mode. Different for each store implementation.
        """
        pass
    pass
