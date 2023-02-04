from volume_dict import vol_units
from lenght_dict import len_units


class Convert:

    def __init__(self):
        self.len_unit = len_units
        self.vol_unit = vol_units

    def convert_length(self, unit_from, unit_to, input_value):
        for i in range(len(len_units)):
            if unit_from in len_units[i]:
                factor = len_units[i][unit_from][unit_to]
                if factor:
                    convert_unit = float(input_value) * factor
                    output = "{0:.3f}".format(convert_unit)
                    return output

    def convert_volume(self, unit_from, unit_to, input_value):
        for i in range(len(vol_units)):
            if unit_from in vol_units[i]:
                factor = vol_units[i][unit_from][unit_to]
                if factor:
                    convert_unit = float(input_value) * factor
                    output = "{0:.3f}".format(convert_unit)
                    return output

    def convert_temperature(self, unit_from, unit_to, input_value):
        if unit_from == "celsius" and unit_to == "fahrenheit":
            convert_unit = ((int(input_value) * 9) / 5) + 32
            output = "{0:.3f}".format(convert_unit)
            return output

        elif unit_from == "celsius" and unit_to == "kelvin":
            convert_unit = (int(input_value) + 273)
            output = "{0:.3f}".format(convert_unit)
            return output

        elif unit_from == "fahrenheit" and unit_to == "celsius":
            convert_unit = (((int(input_value) - 32) * 5) / 9)
            output = "{0:.3f}".format(convert_unit)
            return output

        elif unit_from == "fahrenheit" and unit_to == "kelvin":
            convert_unit = (((int(input_value) - 32) * 5 / 9) + 273)
            output = "{0:.3f}".format(convert_unit)
            return output

        elif unit_from == "kelvin" and unit_to == "celsius":
            convert_unit = (int(input_value) - 273)
            output = "{0:.3f}".format(convert_unit)
            return output

        elif unit_from == "kelvin" and unit_to == "fahrenheit":
            convert_unit = (((int(input_value) - 273) * 9 / 5) + 32)
            output = "{0:.3f}".format(convert_unit)
            return output
