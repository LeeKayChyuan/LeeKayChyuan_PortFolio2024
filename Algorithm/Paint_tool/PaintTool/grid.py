from __future__ import annotations
from typing import TypeVar, Generic
from data_structures.referential_array import ArrayR
from layer_store import LayerStore,SetLayerStore,AdditiveLayerStore,SequenceLayerStore

T = TypeVar('T')

class Grid:
    DRAW_STYLE_SET = "SET"
    DRAW_STYLE_ADD = "ADD"
    DRAW_STYLE_SEQUENCE = "SEQUENCE"
    DRAW_STYLE_OPTIONS = (
        DRAW_STYLE_SET,
        DRAW_STYLE_ADD,
        DRAW_STYLE_SEQUENCE
    )

    DEFAULT_BRUSH_SIZE = 2
    MAX_BRUSH = 5
    MIN_BRUSH = 0
    

    def __init__(self, draw_style, x, y) -> None:
        """
        Initialise the grid object.
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.

        Should also intialise the brush size to the DEFAULT provided as a class variable.
        """
        self.Draw_Style = draw_style
        self.width = x 
        self.height = y
        self.Brush_size = self.DEFAULT_BRUSH_SIZE
        self.grid = ArrayR(x)

        for i in range(x):
            self.grid[i] = ArrayR(y)  

        self.layer_style = None
        
    def __getitem__(self, index: int) -> T:
        """ Returns the object in position index.
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        return self.grid[index]

    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the object in position index to value
        :complexity: O(1)
        :pre: index in between 0 and length - self.array[] checks it
        """
        self.grid[index] = value

    def increase_brush_size(self):
        """
        Increases the size of the brush by 1,
        if the brush size is already MAX_BRUSH,
        then do nothing.
        """
        if self.Brush_size < self.MAX_BRUSH :
            self.Brush_size += 1
        
    def decrease_brush_size(self):
        """
        Decreases the size of the brush by 1,
        if the brush size is already MIN_BRUSH,
        then do nothing.
        """
        if self.Brush_size > self.MIN_BRUSH:
            self.Brush_size -= 1 

    def get_layer_style (self):
        if (self.Draw_Style == self.DRAW_STYLE_SET):
            self.layer_style = SetLayerStore
        if (self.Draw_Style == self.DRAW_STYLE_ADD):
            self.layer_style = AdditiveLayerStore
        if (self.Draw_Style == self.DRAW_STYLE_SEQUENCE):
            self.layer_style = SequenceLayerStore

    def create_layer (self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = self.layer_style()

    def painting_area(self,px,py):
        
        paint_range = self.Brush_size
        upper_coord = []
        lower_coord = []

        for k in range (0, paint_range+1):
            y1 = py + k
            y2 = py - k

            for i in range(0, paint_range+1-k):
                x1 = px + i
                x2 = px - i

                if (y1 & x1) > 0 :
                    upper_coord[i] = [(x1,y1)]
                    
                if (y2 & x2) > 0 :
                    lower_coord[i] = [(x2,y2)]

        return (upper_coord + lower_coord)

    def special(self):
        """
        Activate the special affect on all grid squares.
        """
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y].special()

