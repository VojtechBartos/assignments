class Transformation():
    """Class handle simple data transformation"""

    def remap(self, item):
        """Remapping to a required dict form. 
        :param item: {dict}
        :return: {dict}
        """
        return {
            item['key']: item['value']
        }

    def to_single_object(self, data):
        """Merging list of the dicts to single dict
        :param data: {list}
        :return: {dict}
        """
        output = {}
        for item in data:
            output.update(item)
        return output

    def to_list(self, data):
        """Remap dict to list of tuples
        :param data: {dict}
        :return: {list} of {tuples}
        """
        return sorted(
            [(k, v) for k, v in data.items()], 
            key=lambda k: k[1]
        )

    def execute(self, data):
        """Executing defined transformations
        :param data: {list}
        :return: {list}
        """
        data = map(self.remap, data)
        data = self.to_single_object(data)
        data = self.to_list(data)
        return data