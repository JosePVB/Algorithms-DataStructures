#!/usr/bin/env python3
"""
Module contains the building blocks to create boolean circuits. Specifically,
there are AND, OR, and NOT logic gate classes, as well as a Connector class
that routes the output of one logic gate into the input of another gate.

Jose Vargas 4/28/2018
"""


class LogicGate:
    """
    Simulates input-output boolean algebra relationships, such as in
    digital circuits.

    Assumes that the gate has a single output.

    Children classes exemplify the IS-A Relationship.
    """
    def __init__(self, label):
        """
        Constructor.

        Variables
        ---------
        label, string
        """
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        """Performs the gate logic and returns the output."""
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    """For logic gates that have two inputs."""
    def __init__(self, label):
        """
        Constructor.

        Variables
        ---------
        label, string
        """
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        """
        If pin A is empty, ask the user for the input to the pin; else, the
        pin has been connected, with a Connector, to the output of another
        gate. This output will be the value for this pin.
        """
        if self.pin_a is None:
            return int(input("Enter the input to Pin A "
                             "for gate {}:\t".format(self.get_label())))
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        """
        If pin B is empty, ask the user for the input to the pin; else, the pin
        has been connected, with a Connector, to the output of another gate
        and this output value will be assigned to this pin.
        """
        if self.pin_b is None:
            return int(input("Enter the input to Pin B "
                             "for gate {}:\t".format(self.get_label())))
        else:
            return self.pin_b.get_from().get_output()

    def set_next_pin(self, connection_source):
        """
        Connects an open pin to the output of another logic gate via
        connection_source.

        If no connection is possible, an error is raised.

        Variables
        ---------
        connection_source, Connector instance
        """
        if self.pin_a is None:
            self.pin_a = connection_source
        elif self.pin_b is None:
            self.pin_b = connection_source
        else:
            raise RuntimeError("NO AVAILABLE PINS ON "
                               "{}".format(self.get_label()))


class UnaryGate(LogicGate):
    """For logic gates that have one input."""
    def __init__(self, label):
        """
        Constructor.

        Variables
        ---------
        label, string
        """
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        """
        If the pin is empy, ask the user for the input to the pin; else
        the pin has been connected, with a Connector, to the output of
        another pin.
        """
        if self.pin is None:
            return int(input("Enter the input to the Pin "
                             "for gate {}:\t".format(self.get_label())))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self, connection_source):
        """
        Connects the open pin to the output of another logic gate via
        connection_source; raises an error otherwise.

        Variables
        ---------
        connection_source, Connector instance
        """
        if self.pin is None:
            self.pin = connection_source
        else:
            raise RuntimeError("PIN IS NOT AVAILABLE ON "
                               "{}".format(self.get_label()))


class AndGate(BinaryGate):
    """If one or more of the inputs is 0, the logic gate returns 0."""
    def __init__(self, label):
        """
        Constructor.

        Variables
        ---------
        label, string
        """
        super().__init__(label)

    def perform_gate_logic(self):
        """Computes the output given two user inputs."""
        self.get_pin_a()
        self.get_pin_b()

        if self.pin_a and self.pin_b == 1:
            return 1
        return 0


class OrGate(BinaryGate):
    """If one or more of the inputs is 1, the logic gate returns 1."""
    def __init__(self, label):
        """
        Constructor.

        Variables
        ---------
        label, string
        """
        super().__init__(label)

    def perform_gate_logic(self):
        """Computes the output given two user inputs."""
        self.get_pin_a()
        self.get_pin_b()

        if self.pin_a or self.pin_b == 1:
            return 1
        return 0


class NotGate(UnaryGate):
    """Return the opposite value of the input."""
    def __init__(self, label):
        """
        Constructor.

        Variables
        ---------
        label, string
        """
        super().__init__(label)

    def perform_gate_logic(self):
        """Computes the output given a user input."""
        self.get_pin()

        if self.pin == 0:
            return 1
        return 0


class Connector:
    """
    Connects the output of one logic gate to the input of another gate.

    Exemplifies the HAS-A Relationship.
    """
    def __init__(self, from_gate, to_gate):
        """
        Constructor.

        Variables
        ---------
        from_gate, LogicGate grandchild instance
            The gate whose output needs to be routed.
        to_gate, LogicGate grandchild instance
            The gate that will receive the output.
        """
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


if __name__ == '__main__':
    # Example circuit. Call g4.get_output() to run the circuit.

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
