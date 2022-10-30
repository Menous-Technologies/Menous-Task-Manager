import json
from pathlib import Path
import os

dir = os.path.join(Path(__file__).parent, 'database')

if not os.path.exists(dir):
    os.mkdir(dir)


if not os.path.exists(dir + '/data.json'):
    with open(dir + '/data.json', 'w') as file:
        json.dump([], file, indent=True)


if not os.path.exists(dir + '/auth.json'):
    with open(dir + '/auth.json', 'w') as file:
        json.dump({}, file, indent=True)


def getData(project= None):
    if project  ==  None:
        with open(dir+'/data.json') as file:
            return json.load(file)
    else:
        project  = project.lower()
        if os.path.exists(dir + f'/{project}.json'):
            with open(dir + f'/{project}.json') as file:
                return json.load(file)
        raise Exception('Project file not found')


def writeData(data, project=None):
    if project == None:
        with open(dir+'/data.json', 'w') as file:
            json.dump(data,file, indent=4)
    else:

        if os.path.exists(dir + f'/{project.lower()}.json'):
            with open(dir + f'/{project.lower()}.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            raise Exception('Project file not found')


def createProject(project):
    path = dir+f'/{project.lower()}.json'
    if os.path.exists(path):
        raise Exception('Already exists')
    else:
        with open(path, 'w') as file:
            json.dump([],file)


def addTask(title, description, tag, deadline, project=None):

    if project == None:
        data = getData()
        for i in data:
            if i['title'] == title:
                raise Exception('Task Already Created')
        task = {
            'title':title,
            'description':description,
            'tag':tag,
            'deadline': deadline,
        }
        data.append(task)
        writeData(data)

    else:
        data = getData(project=project)
        for i in data:
            if i['title'] == title:
                raise Exception('Task Already Created')
        task = {
            'title':title,
            'description':description,
            'tag':tag,
            'deadline': deadline,
        }
        data.append(task)
        writeData(data, project = project)


