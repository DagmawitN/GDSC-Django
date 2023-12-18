#Task1
def basic_operation(num1 , num2) :
    try:
        dic= {"adddition" : num1+num2 , 
              "subtraction " : num1-num2 , 
              "multiplication " : num1*num2 , 
              "Division " : num1/num2}
       
    except ZeroDivisionError:
        dic = {"error" : "Divsion by zero is not allowed"}
        return None
    except Exception as e :
        print ("Error:" , str(e))
        return None
    return dic
def power_operation(base , exponent,**kwargs) :
    try:
        result = base ** exponent
        if "modulo" in kwargs :
            modulo_value = kwargs['modulo']
            result = result % modulo_value
        return result
    except Exception as e:
        print ("Error:" , str(e))
        return None
def apply_operations(li):
    result = []
    for op in li:
        function = op[0]
        arguments = op[1:]
        try:
            result = function(*arguments) 
            result.append(result)
        except Exception as e:
            print ("Error:" , str(e))
            result.append(None)
    return result

print (basic_operation(5,5))
print(power_operation(5 , 3 ))
#task2
import os
import shutil
import time

def get_files_in_last_24_hours(directory):
    current_time = time.time()
    twenty_four_hours_ago = current_time - 24 * 60 * 60
    files_in_last_24_hours = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_stat = os.stat(file_path)
            file_modified_time = file_stat.st_mtime
            file_created_time = file_stat.st_ctime

            if file_modified_time > twenty_four_hours_ago or file_created_time > twenty_four_hours_ago:
                files_in_last_24_hours.append(file_path)

    return files_in_last_24_hours

def update_files(files):
    for file_path in files:
        with open(file_path, 'a') as file:
            file.write("\nModified at: " + time.ctime())

def create_last_24hours_folder(directory):
    folder_path = os.path.join(directory, "last_24hours")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

def move_files(files, destination_directory):
    for file_path in files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination_directory, file_name)
        shutil.move(file_path, destination_path)

current_directory = os.getcwd()
files_in_last_24_hours = get_files_in_last_24_hours(current_directory)
update_files(files_in_last_24_hours)
destination_directory = create_last_24hours_folder(current_directory)
move_files(files_in_last_24_hours, destination_directory)
