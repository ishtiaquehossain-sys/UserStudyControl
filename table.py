import parameter
from shape import Shape


class Table(Shape):
    def __init__(self):
        super(Table, self).__init__()

    def setup_parameter_vector(self):
        """
        Define the parameter vector in this function
        Use the following format when adding element to the parameter vector
        self.add_parameter_vector_element
            (name_of_parameter,             # String, specifying name of the parameter
            type_of_parameter,              # 's', 'i' or 'b', for scalar, integer or binary respectively
            minimum_allowable_value,        # Ignore if binary parameter
            maximum_allowable_value)        # Ignore if binary parameter
        """
        return

    def procedure(self, param_vector: parameter.ParameterVector):
        # Implement your procedure for the table class in this function
        return

    def specify_parameter_vectors(self):
        """
        Specify the parameter vectors in this function
        Use the following format when specifying a parameter vector
        self.assign_parameter_vector_to_shape
            (index,                         # Integer, specifying the index of the shape
            parameter_vector)               # List of elements, representing the parameter vector
        """
        return
