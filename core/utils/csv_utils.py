import traceback

from core.utils.utils import logstd


class CSVUtils:

    @staticmethod
    def write(filename: str, field_names: tuple, data: list, delimiter: str = ';') -> str:
        file_object = None
        try:
            file_object = open(filename, 'w')

            # Write header
            file_object.write((';').join(field_names))
            file_object.write("\n")

            # Write rows
            output_data = ''
            for row in data:
                first = True
                for i, j in enumerate(row):
                    if j in field_names:
                        field = row[j]
                        if type(field) == int or type(field) == float:
                            output_data += f"{delimiter if not first else ''}{field}"
                        else:
                            output_data += f"{delimiter if not first else ''}\"{field}\""
                        first = False

                output_data += "\n"

            file_object.write(output_data)
            file_object.close()

            return filename
        except Exception as e:
            traceback.print_exc()
            logstd(e)
            return -1
        finally:
            file_object.close()
