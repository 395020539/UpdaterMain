import json
from configuration_reader import MyConfig
from database_hander import MyDataBaseHander


class MyDxlCommand:
    def __init__(self):
        myconfig = MyConfig()
        self.path_suffix = myconfig.data_suffix
        self.doors_project_path = myconfig.doors_project_path



    def create_update_dxl(self, data_list):
        mydbo = MyDataBaseHander()
        list_dxl_command_temp = []
        list_dxl_command = []
        print("dic_data len:", len(data_list))

        dxl_open_module = """
    Module m = edit(DOORS_MODULE, false)
    Object o
    string DATA_NAME = ""
    string DATA_VALUE = ""
                """

        dxl_update_data = """
    for o in all(m) do {
        if (o."Object Text" "" == DATA_NAME){
            o."Wert(e)" = DATA_VALUE
        }
    }
                        """

        dxl_end = """
    save(m)
    close(m)
    return_ "0"
                    """

        for data in data_list:
            data_name = data[0]
            module_name = data[1]
            data_value = data[2]
            print("data name = ", data_name)
            print("module_name = ", module_name)
            print("data_value = ", data_value)

            data_module_path = mydbo.query_path(data_name, module_name)
            doors_module = '"{}{}"'.format(self.doors_project_path, data_module_path + self.path_suffix)
            print("doors_module = ", doors_module)

            dxl_declare_module = "const string DOORS_MODULE = {}".format(doors_module)
            print("dxl_declare_module =", dxl_declare_module)

            dxl_declare_data = """
    DATA_NAME = "{}"
    DATA_VALUE = "{}"
                            """.format(data_name, data_value)

            dxl_update_date_command = dxl_declare_module + dxl_open_module + dxl_declare_data + dxl_update_data + dxl_end
            print("dxl_update_date_command = ", dxl_update_date_command)

            list_dxl_command_temp.append(dxl_update_date_command)
            print("list_dxl_command_temp = ", list_dxl_command_temp)
            print("number of command = ", len(list_dxl_command_temp))

        for dxl_command in list_dxl_command_temp:
            # print(dxl_command)
            # index = list_dxl_command_temp.index(dxl_command)
            # print("index = {}".format(index))
            # print(type(dxl_command))
            new_dxl_command = bytes(dxl_command, encoding='utf-8')
            # print(new_dxl_command)
            # list_dxl_command[index] = new_dxl_command
            list_dxl_command.append(new_dxl_command)
        print("list_dxl_command = \n", list_dxl_command)

        return list_dxl_command

    def find_value(self, data_name, module_name):
        mydbo = MyDataBaseHander()
        data_module_path = mydbo.query_path(data_name, module_name)
        doors_module = '"{}{}"'.format(self.doors_project_path, data_module_path + self.path_suffix)
        print("doors_module = ", doors_module)

        dxl_declare_module = "const string DOORS_MODULE = {}".format(doors_module)

        dxl_open_module = """
    Module m = read(DOORS_MODULE, false)
    Object o
    string DATA_NAME = "{}" """.format(data_name)
        dxl_content = """       
    string DATA_VALUE = ""
    for o in all(m) do {
        if (o."Object Text" "" == DATA_NAME){
                DATA_VALUE = o."Wert(e)" 
            }
        }   
    close m
    return_ DATA_VALUE"""

        dxl_update_date_command = dxl_declare_module + dxl_open_module + dxl_content
        print("dxl_update_date_command = ", dxl_update_date_command)

        dxl_command = bytes(dxl_update_date_command, encoding='utf-8')
        print("dxl_command = \n", dxl_command)

        return dxl_command

    def read_json_data(self, data_file):
        json_data = ""
        data_json_path = data_file
        try:
            with open(data_json_path, 'r') as f:
                json_data = json.load(f)
                print(f"json_data = \n{json_data}")
        except Exception as e:
            print("An error occurred:", e)
        dic_data = json_data
        print(f"dic_data = \n{dic_data}")

        return dic_data


if __name__ == '__main__':
    dxl_commands = MyDxlCommand()
    print("dxl_commands: ", dxl_commands)

    data_name = "Speed_Invalid_Signal"
    module_name = "ASM"
    dxl_command = dxl_commands.find_value(data_name, module_name)
