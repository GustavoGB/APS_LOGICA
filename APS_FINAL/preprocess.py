import sys
import re
from main import *

class PrePro:    
    @staticmethod
    def filter(codigo):
        codigo_filtrado = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "",codigo)
        codigo_filtrado = re.sub("\n", "", codigo_filtrado)
        return codigo_filtrado
