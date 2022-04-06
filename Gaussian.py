import math
import matplotlib.pyplot as plt


class Gaussian:
    """Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
    """
    def __init__(self, mu = 0, sigma = 1):
        self.mean = mu
        self.stdev = sigma
        self.data = []

    def calculate_mean(self) -> float:
        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set
        """
        sum= 0
        for item in self.data:
            sum += item

        return sum / len(self.data)

    def calculate_stdev(self, sample=True) -> float:
        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation
        """
        mean = self.calculate_mean()
        sum_of_squares = 0
        for item in self.data:
            deviation = (item - mean)
            deviation *= deviation
            sum_of_squares += deviation
        if sample:
            variance = sum_of_squares / (len(self.data) - 1)
        else:
            variance = sum_of_squares / len(self.data)
        return math.sqrt(variance)