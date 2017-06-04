import numpy as np


class GachonLPSolver:
    MAXIMIZE = 0
    MINIMIZE = 1
    LESSEQUAL = 1
    EQUAL = 0
    GRATERQUAL = -1

    def __init__(self, model_name):
        self._model_name = model_name
        self._objective_variables = None
        self._optimize_setting = None
        self._standard_form_matrix = None
        self._constraints_coefficient_matrix = None
        self._constraints_sign_list = []
        self._basic_variables_index = None
        self._non_basic_variables_index = None

    def set_objective_variables(self, objective_coefficient_vector, optimize_setting):
        pass

    def add_constraints(self, constraints_coefficient_vector, sign, rhs):
        pass

    def update(self):
        pass

    def optimize(self):
        pass

    def gauss_jordan_elimination_process(self, pivot_row_position, column_position):
        matrix_row_size = self._standard_form_matrix.shape[0]
        pivot_value = self._standard_form_matrix[pivot_row_position, column_position]
        if pivot_value < 0:
            self._standard_form_matrix[pivot_row_position, :] = -1 * self._standard_form_matrix[
                pivot_row_position, column_position]

        for i in range(matrix_row_size):
            if i != pivot_row_position:
                target_value = self._standard_form_matrix[i][column_position]
                compensating_value = -1 * (target_value / pivot_value)
                pivot_row = compensating_value * self._standard_form_matrix[pivot_row_position, :]
                self._standard_form_matrix[i] += pivot_row

    def get_z_value(self):
        pass

    def get_objective_variables(self):
        pass

    @property
    def standard_form_matrix(self):
        return self._standard_form_matrix

    @property
    def model_name(self):
        return self._model_name

    @property
    def objective_variables(self):
        return self._objective_variables

    @property
    def constraints_coefficient_matrix(self):
        return self._constraints_coefficient_matrix

    @property
    def constraints_sign_list(self):
        return self._constraints_sign_list


def model_name():
    # This is a mock test function.Do NOT need to modify it.
    pass

def set_objective_variables():
    # This is a mock test function.Do NOT need to modify it.
    pass

def add_constraints():
    # This is a mock test function.Do NOT need to modify it.
    pass

def update(self):
    # This is a mock test function.Do NOT need to modify it.
    pass

def optimize_easy(self):
    # This is a mock test function.Do NOT need to modify it.
    pass

def optimize_hard(self):
    # This is a mock test function.Do NOT need to modify it.
    pass

