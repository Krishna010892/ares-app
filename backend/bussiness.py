# Building a logic for api
# print("HELLO DEVOPS ENGINEER FROM PYTHON 3.11 ALPINE v3")
def get_data():

    with open('names.txt') as f:

        names=f.read()

        names=names.split()

        return names

        # for i, name in enumerate(names):

        #     print(f"{i+1}.{name}")

        # print(names)