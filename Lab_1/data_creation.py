import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42
SAMPLE_SIZE = 1000

# Функция для моделирования
def paint_drying_time(temperature, humidity):
    return 24 - 0.5 * temperature + 0.2 * humidity

# Создаем папки train и test, если их еще не существует
if not os.path.exists('train'):
    os.makedirs('train')
if not os.path.exists('test'):
    os.makedirs('test')
    