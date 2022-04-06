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

    def read_data_file(self, file_name, sample=True):
        """Method to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
        After reading in the file, the mean and standard deviation are calculated

        Args:
            file_name (string): name of a file to read from

        Returns:
            None
        """

        # This code opens a data file and appends the data to a list called data_list
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        # Copy data_list to self.data attribute
        self.data = data_list.copy()
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        """Method to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """