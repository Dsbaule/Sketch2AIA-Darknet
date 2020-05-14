import json
from zipfile import ZipFile
from src.AIA import AIAProject


def generateAIAJson(screen: AIAProject.Screen):
    return convertJson(json.dumps(screen.toDict()))


def convertJson(originalJson):
    return \
        '#|\n' + \
        '$JSON\n' + \
        originalJson + '\n' \
                       '|#'


def saveFile(project: AIAProject.Project):
    savePath = './Result/' + project.AppName + '.aia'

    with ZipFile(savePath, 'x') as myzip:
        with myzip.open("youngandroidproject/project.properties", 'w') as project_properties_file:
            project_properties_file.write(bytes(project.genProperties(), 'utf-8'))
        for Screen in project.Screens:
            with myzip.open('src/appinventor/sketch2aia/' + project.AppName + '/' + Screen.Name + '.scm',
                            'w') as screenScmFile:
                screenScmFile.write(bytes(generateAIAJson(Screen), 'utf-8'))
            with myzip.open('src/appinventor/ai_dsbaule/' + project.AppName + '/' + Screen.Name + '.bky',
                            'w') as screenBkyFile:
                screenBkyFile.write(bytes('', 'utf-8'))