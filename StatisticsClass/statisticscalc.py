import math

class StatisticsCalc:
    def __init__(self, data_list):
        self.data = data_list
        self.data_size = len(data_list)
        self._mean = None
        self._std = None
        self._standard_uncertainty = None
        self._low = None
        self._high = None
    
    @property
    def mean(self):
        if self._mean is None:
            self._mean = sum(self.data) / self.data_size
        return self._mean
    
    @property
    def standard_deviation(self):
        if self._std is None:
            sum_of_differences = sum((data - self.mean) ** 2 for data in self.data)
            std_squared = sum_of_differences / (self.data_size - 1)
            self._std = math.sqrt(std_squared)
        return self._std
    
    @property
    def standard_uncertainty(self):
        if self._standard_uncertainty is None:
            self._standard_uncertainty = self.standard_deviation / math.sqrt(self.data_size)
        return self._standard_uncertainty
    
    @property
    def low(self):
        if self._low is None:
            self._low = self.mean - (2 * self.standard_uncertainty)
        return self._low
    
    @property
    def high(self):
        if self._high is None:
            self._high = self.mean + (2 * self.standard_uncertainty)
        return self._high